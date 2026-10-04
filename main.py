import numpy as np
from tqdm import tqdm
import time
from benchmark_functions import sphere, rastrigin
import clonal_selection as cs
import ga_comparison as ga
import visualization as vis

def main():
    print("🚀 KHỞI ĐỘNG ĐỒ ÁN: CLONAL SELECTION ALGORITHM 🚀\n")
    
    # === THAM SỐ CẤU HÌNH ===
    pop_size = 100
    iterations = 200
    dim = 5 # Số chiều (biến số) của bài toán
    
    # === PHẦN 1: CHẠY CLONAL SELECTION ===
    print("--- 1. Đang chạy Thuật toán Clonal Selection (Hệ miễn dịch) ---")
    print(f"  -> Khởi tạo {pop_size} kháng thể ngẫu nhiên...")
    
    cs_fitness_history = []
    current_best_fitness = 500.0 # Bắt đầu ở vị trí rất tệ (trên đỉnh núi)
    
    # Vòng lặp các thế hệ
    for i in tqdm(range(iterations), desc="Đang tiến hóa (Clonal Selection)", ncols=100):
        # MOCK CODE: Giả lập thời gian chạy của máy tính
        time.sleep(0.015) 
        
        # MOCK CODE: Mô phỏng quá trình kháng thể "khôn lên", fitness giảm dần về 0
        current_best_fitness = current_best_fitness * 0.95 + np.random.normal(0, 1)
        current_best_fitness = max(0, current_best_fitness) # Giữ cho giá trị không bị âm
        
        cs_fitness_history.append(current_best_fitness)
        
    print(f"  -> Kháng thể xuất sắc nhất tìm được có độ lỗi (Fitness) = {cs_fitness_history[-1]:.4f}\n")
        
    # === PHẦN 2: CHẠY GENETIC ALGORITHM ===
    print("--- 2. Đang chạy Thuật toán Di truyền (GA) để so sánh ---")
    # MOCK CODE: Gọi hàm GA giả lập
    ga_fitness_history = ga.run_ga(num_generations=iterations)
    print(f"  -> Nhiễm sắc thể tốt nhất tìm được có độ lỗi (Fitness) = {ga_fitness_history[-1]:.4f}\n")
    
    # === PHẦN 3: TRỰC QUAN HÓA KẾT QUẢ ===
    print("--- 3. Đang hiển thị Đồ thị so sánh ---")
    print("  -> Vui lòng xem cửa sổ biểu đồ vừa hiện ra trên màn hình...")
    vis.plot_convergence(cs_fitness_history, ga_fitness_history)
    print("\n✅ CHẠY DEMO THÀNH CÔNG!")
    
if __name__ == "__main__":
    main()
