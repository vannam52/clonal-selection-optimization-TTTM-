import numpy as np

def init_population(pop_size, dim, bounds):
    """
    Khởi tạo quần thể kháng thể ngẫu nhiên.
    (Nhiệm vụ của Người số 1)
    """
    # Lấy giá trị nhỏ nhất và lớn nhất từ bounds, ví dụ (-5.12, 5.12)
    min_val, max_val = bounds
    
    # Dùng Numpy tạo ma trận ngẫu nhiên đều (uniform) kích thước (pop_size hàng x dim cột)
    population = np.random.uniform(min_val, max_val, size=(pop_size, dim))
    
    return population

def evaluate_fitness(population, fitness_func):
    """
    Đánh giá độ thích nghi (affinity) của từng kháng thể.
    (Nhiệm vụ của Người số 1)
    """
    # Tạo mảng rỗng chứa điểm của tất cả kháng thể
    fitness_scores = np.zeros(population.shape[0])
    
    # Duyệt qua từng kháng thể và cho điểm nó bằng hàm mục tiêu (Sphere/Rastrigin)
    for i in range(population.shape[0]):
        fitness_scores[i] = fitness_func(population[i])
        
    return fitness_scores

def clone(population, fitness, clone_rate=0.5):
    """
    Nhân bản các kháng thể tốt. Kháng thể có điểm càng tốt (thấp) thì nhân bản càng nhiều.
    (Nhiệm vụ của Người số 2)
    """
    pop_size = population.shape[0]
    
    # Sắp xếp index của fitness từ thấp (tốt) đến cao (dở)
    sorted_indices = np.argsort(fitness)
    
    clones = []
    clone_fitnesses = []
    
    # Duyệt qua từng kháng thể đã được xếp hạng
    for rank, idx in enumerate(sorted_indices):
        # Công thức: Hạng 1 (rank 0) sẽ được nhân nhiều nhất. Càng về sau số lượng clone càng giảm.
        # Ví dụ pop_size=100, rank 0 -> 50 clone, rank 49 -> 1 clone.
        num_clones = int(clone_rate * pop_size / (rank + 1))
        
        # Đảm bảo ít nhất mỗi cá thể được giữ lại 1 bản sao
        num_clones = max(1, num_clones) 
        
        for _ in range(num_clones):
            clones.append(population[idx].copy())
            clone_fitnesses.append(fitness[idx])
            
    return np.array(clones), np.array(clone_fitnesses)

def mutate(clones, clone_fitnesses, mutation_rate, bounds):
    """
    Đột biến các bản sao. Kháng thể tốt đột biến ít, kháng thể dở đột biến nhiều.
    (Nhiệm vụ của Người số 2)
    """
    min_val, max_val = bounds
    mutated_clones = np.zeros_like(clones)
    
    # Tìm Max và Min của fitness để chuẩn hóa về thang điểm [0, 1]
    f_min = np.min(clone_fitnesses)
    f_max = np.max(clone_fitnesses)
    
    for i in range(clones.shape[0]):
        # Chuẩn hóa điểm: alpha gần 0 -> kháng thể tốt; alpha gần 1 -> kháng thể dở
        if f_max == f_min:
            alpha = 0.5
        else:
            alpha = (clone_fitnesses[i] - f_min) / (f_max - f_min)
            
        # Tính độ mạnh của đột biến. Cộng thêm 0.05 để đảm bảo kháng thể xịn nhất vẫn xê dịch 1 tí.
        sigma = mutation_rate * (alpha + 0.05)
        
        # Sinh ra sự biến đổi ngẫu nhiên theo phân phối chuẩn (Gaussian)
        mutation_shift = np.random.normal(0, sigma, size=clones.shape[1])
        
        # Cộng sự biến đổi vào bản sao
        mutated_clones[i] = clones[i] + mutation_shift
        
    # Ép tọa độ không cho văng ra khỏi khu vực tìm kiếm (VD: không vượt quá 5.12)
    mutated_clones = np.clip(mutated_clones, min_val, max_val)
    
    return mutated_clones

def select(population, pop_fitness, mutated_clones, mutated_fitnesses, pop_size):
    """
    Trận chiến sinh tồn: Chọn lọc top những kháng thể xuất sắc nhất cho thế hệ tiếp theo.
    """
    # Gộp dân số cũ và các bản sao mới bị đột biến lại làm 1 đấu trường
    combined_pop = np.vstack((population, mutated_clones))
    combined_fit = np.concatenate((pop_fitness, mutated_fitnesses))
    
    # Sắp xếp điểm toàn bộ đấu trường từ thấp (tốt) đến cao (dở)
    sorted_indices = np.argsort(combined_fit)
    
    # Lấy đúng số lượng pop_size (VD: 100) cá thể đứng đầu làm thế hệ F1
    best_indices = sorted_indices[:pop_size]
    
    next_population = combined_pop[best_indices]
    next_fitness = combined_fit[best_indices]
    
    return next_population, next_fitness

def receptor_editing(population, fitness, edit_rate, bounds):
    """
    Receptor Editing: Loại bỏ các kháng thể tồi nhất và thay thế bằng kháng thể tạo ngẫu nhiên.
    Giúp duy trì sự đa dạng của quần thể, tránh bị kẹt ở điểm cực tiểu cục bộ (local minima).
    """
    pop_size, dim = population.shape
    num_edit = int(pop_size * edit_rate)
    
    # Sắp xếp điểm toàn bộ đấu trường từ thấp (tốt) đến cao (dở)
    sorted_indices = np.argsort(fitness)
    
    # Giữ lại những cá thể tốt, loại bỏ `num_edit` cá thể dở nhất ở cuối danh sách
    best_indices = sorted_indices[:-num_edit]
    
    # Sinh ra `num_edit` cá thể mới hoàn toàn ngẫu nhiên
    min_val, max_val = bounds
    new_antibodies = np.random.uniform(min_val, max_val, size=(num_edit, dim))
    
    # Gộp cá thể tốt cũ và cá thể mới lại
    edited_population = np.vstack((population[best_indices], new_antibodies))
    
    return edited_population
