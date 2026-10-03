import numpy as np
from tqdm import tqdm
from benchmark_functions import sphere, rastrigin
import clonal_selection as cs
import ga_comparison as ga
import visualization as vis

def main():
    print("🚀 Khởi động Đồ án Clonal Selection Algorithm...")
    
    # === THAM SỐ CẤU HÌNH ===
    pop_size = 100
    iterations = 200
    dim = 5 # Số chiều (biến số) của bài toán
    bounds = (-5.12, 5.12)
    
    # === PHẦN 1: CHẠY CLONAL SELECTION ===
    print("\n--- 1. Đang chạy Thuật toán Clonal Selection ---")
    cs_fitness_history = []
    
    # TODO: Khởi tạo quần thể ban đầu
    # population = cs.init_population(pop_size, dim, bounds)
    
    for i in tqdm(range(iterations), desc="Tiến trình Clonal Selection"):
        # TODO: Cập nhật hàm đánh giá, clone, mutate ở đây
        # cs_fitness_history.append(best_fitness)
        pass
        
    # === PHẦN 2: CHẠY GENETIC ALGORITHM ===
    print("\n--- 2. Đang chạy Thuật toán Di truyền (GA) để so sánh ---")
    ga_fitness_history = []
    # TODO: Gọi hàm run_ga
    # ga_fitness_history = ga.run_ga(...)
    
    # === PHẦN 3: TRỰC QUAN HÓA KẾT QUẢ ===
    print("\n--- 3. Đang hiển thị Đồ thị so sánh ---")
    # vis.plot_convergence(cs_fitness_history, ga_fitness_history)
    
if __name__ == "__main__":
    main()
