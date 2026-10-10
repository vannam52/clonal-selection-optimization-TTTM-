import numpy as np
from tqdm import tqdm
import time
from benchmark_functions import sphere, rastrigin
import clonal_selection as cs
import ga_comparison as ga
import visualization as vis

def run_experiment(benchmark_func, pop_size=100, iterations=200, dim=5, bounds=(-5.12, 5.12)):
    """
    Hàm đóng gói quy trình chạy thử nghiệm cho 1 bài toán (Sphere hoặc Rastrigin)
    """
    func_name = benchmark_func.__name__.capitalize()
    print(f"\n{'='*60}")
    print(f"🚀 BẮT ĐẦU THỬ NGHIỆM VỚI HÀM: {func_name.upper()} 🚀")
    print(f"{'='*60}")
    
    # === PHẦN 1: CHẠY CLONAL SELECTION ===
    print("\n--- 1. Đang chạy Thuật toán Clonal Selection (Hệ miễn dịch) ---")
    cs_fitness_history = []
    
    population = cs.init_population(pop_size, dim, bounds)
    fitness = cs.evaluate_fitness(population, benchmark_func)
    
    for i in tqdm(range(iterations), desc=f"Tiến hóa CS ({func_name})", ncols=100):
        clones, clone_fitnesses = cs.clone(population, fitness, clone_rate=0.5)
        mutated_clones = cs.mutate(clones, clone_fitnesses, mutation_rate=3.0, bounds=bounds)
        mutated_fitnesses = cs.evaluate_fitness(mutated_clones, benchmark_func)
        population, fitness = cs.select(population, fitness, mutated_clones, mutated_fitnesses, pop_size)
        
        # Bổ sung Receptor Editing (Thay thế 10% tồi nhất bằng cá thể mới)
        population = cs.receptor_editing(population, fitness, edit_rate=0.1, bounds=bounds)
        fitness = cs.evaluate_fitness(population, benchmark_func)
        
        cs_fitness_history.append(np.min(fitness))
        
    print(f"  -> Kháng thể xịn nhất tìm được (Điểm lỗi) = {cs_fitness_history[-1]:.4f}")
        
    # === PHẦN 2: CHẠY GENETIC ALGORITHM ===
    print("\n--- 2. Đang chạy Thuật toán Di truyền (GA) để so sánh ---")
    ga_fitness_history = ga.run_ga(
        benchmark_func=benchmark_func, 
        num_generations=iterations, 
        pop_size=pop_size, 
        dim=dim, 
        bounds=bounds
    )
    print(f"  -> Nhiễm sắc thể xịn nhất tìm được (Điểm lỗi) = {ga_fitness_history[-1]:.4f}")
    
    # === PHẦN 3: TRỰC QUAN HÓA KẾT QUẢ ===
    print(f"\n--- 3. Bật đồ thị so sánh cho bài toán {func_name} ---")
    vis.plot_convergence(cs_fitness_history, ga_fitness_history, func_name)


def main():
    print("🚀 KHỞI ĐỘNG ĐỒ ÁN: CLONAL SELECTION ALGORITHM 🚀\n")
    
    # Chạy kịch bản 1: Hàm Sphere (Bài toán dễ, cái chảo láng mịn)
    # run_experiment(sphere)
    
    # Chạy kịch bản 2: Hàm Rastrigin (Bài toán khó, nhiều hố bẫy)
    run_experiment(rastrigin)
    
    print("\n✅ HOÀN THÀNH TOÀN BỘ CÁC BÀI TEST!")

if __name__ == "__main__":
    main()
