import numpy as np
import pygad

# Mảng toàn cục lưu lịch sử điểm để vẽ đồ thị
ga_history = []

def run_ga(benchmark_func, num_generations=200, pop_size=100, dim=5, bounds=(-5.12, 5.12)):
    """
    Chạy thuật toán Di truyền bằng thư viện PyGAD để so sánh.
    (Nhiệm vụ của Người số 3)
    """
    global ga_history
    ga_history = [] # Reset mảng mỗi lần chạy
    
    # Hàm đánh giá (Fitness Function) dành riêng cho PyGAD
    # Lưu ý: PyGAD luôn tìm giá trị LỚN NHẤT. Nhưng bài toán Sphere tìm giá trị NHỎ NHẤT (về 0)
    # => Phải lật ngược điểm: 1 / (điểm Sphere + 1e-8)
    def fitness_func(ga_instance, solution, solution_idx):
        error = benchmark_func(solution)
        return 1.0 / (error + 1e-8)

    # Hàm Camera (Callback): Được gọi mỗi khi tiến hóa xong 1 thế hệ
    def on_generation(ga_instance):
        # Lấy cá thể tốt nhất của thế hệ hiện tại
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        # Tính lại điểm lỗi thật sự (chưa bị lật ngược) để vẽ đồ thị cho chuẩn
        real_error = benchmark_func(solution)
        ga_history.append(real_error)

    # Thiết lập cấu hình GA (Đảm bảo cân kèo với Clonal Selection)
    ga_instance = pygad.GA(
        num_generations=num_generations,
        num_parents_mating=int(pop_size / 2), # Chọn 50% cá thể giỏi nhất để lai ghép
        fitness_func=fitness_func,
        sol_per_pop=pop_size,                 # 100 cá thể
        num_genes=dim,                        # 5 chiều
        init_range_low=bounds[0],             # Giới hạn dưới
        init_range_high=bounds[1],            # Giới hạn trên
        mutation_percent_genes=20,            # Tỷ lệ đột biến 20%
        on_generation=on_generation,          # Gắn camera theo dõi
        suppress_warnings=True                # Tắt các cảnh báo lặt vặt
    )
    
    # Kích hoạt quá trình tiến hóa
    ga_instance.run()
    
    return ga_history
