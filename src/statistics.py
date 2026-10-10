from benchmark_functions import rastrigin
import numpy as np
import time
from tqdm import tqdm
#from benchmark_functions import sphere
import clonal_selection as cs
import ga_comparison as ga

def run_cs_once(benchmark_func, pop_size=100, iterations=200, dim=5, bounds=(-5.12, 5.12)):
    """Chạy Clonal Selection 1 lần và trả về kết quả cuối cùng (không in log, không vẽ hình)"""
    population = cs.init_population(pop_size, dim, bounds)
    fitness = cs.evaluate_fitness(population, benchmark_func)
    
    for _ in range(iterations):
        clones, clone_fitnesses = cs.clone(population, fitness, clone_rate=0.5)
        mutated_clones = cs.mutate(clones, clone_fitnesses, mutation_rate=0.5, bounds=bounds)
        mutated_fitnesses = cs.evaluate_fitness(mutated_clones, benchmark_func)
        population, fitness = cs.select(population, fitness, mutated_clones, mutated_fitnesses, pop_size)
        population = cs.receptor_editing(population, fitness, edit_rate=0.1, bounds=bounds)
        fitness = cs.evaluate_fitness(population, benchmark_func)
        
    return np.min(fitness)

def run_statistical_analysis(num_runs=30):
    print(f"🔄 Đang tiến hành chạy thống kê {num_runs} lần độc lập...")
    
    cs_results = []
    ga_results = []
    cs_times = []
    ga_times = []
    
    for i in tqdm(range(num_runs), desc="Đang phân tích", ncols=100):
        # 1. Đánh giá Clonal Selection
        start_time = time.time()
        #cs_best = run_cs_once(sphere)
        cs_best = run_cs_once(rastrigin)
        cs_times.append(time.time() - start_time)
        cs_results.append(cs_best)
        
        # 2. Đánh giá Genetic Algorithm (Tắt log để chạy ngầm)
        start_time = time.time()
        #ga_history = ga.run_ga(sphere, num_generations=200, pop_size=100, dim=5, bounds=(-5.12, 5.12))
        ga_history = ga.run_ga(rastrigin, num_generations=200, pop_size=100, dim=5, bounds=(-5.12, 5.12))
        ga_times.append(time.time() - start_time)
        ga_results.append(ga_history[-1])
        
    # Xử lý số liệu và in Bảng Thống Kê
    print("\n" + "="*75)
    print(f"📊 BẢNG THỐNG KÊ KẾT QUẢ SAU {num_runs} LẦN CHẠY (HÀM RASTRIGIN) 📊")
    print("="*75)
    print(f"{'Tiêu chí':<25} | {'Clonal Selection (HMD)':<22} | {'Genetic Algorithm'}")
    print("-" * 75)
    print(f"{'Tốt nhất (Best)':<25} | {np.min(cs_results):<22.6f} | {np.min(ga_results):.6f}")
    print(f"{'Tệ nhất (Worst)':<25} | {np.max(cs_results):<22.6f} | {np.max(ga_results):.6f}")
    print(f"{'Trung bình (Mean)':<25} | {np.mean(cs_results):<22.6f} | {np.mean(ga_results):.6f}")
    print(f"{'Độ lệch chuẩn (Std Dev)':<25} | {np.std(cs_results):<22.6f} | {np.std(ga_results):.6f}")
    print("-" * 75)
    print(f"{'Thời gian TB/lần chạy':<25} | {np.mean(cs_times):<19.4f}s | {np.mean(ga_times):.4f}s")
    print("="*75)
    
    print("\n💡 Phân tích điểm:")
    print("- Điểm Trung bình (Mean) & Tốt nhất (Best) càng gần 0 càng tuyệt vời.")
    print("- Độ lệch chuẩn (Std Dev) càng nhỏ chứng tỏ tính ổn định của thuật toán càng cao.")
    print("- Thời gian xử lý cho thấy độ cồng kềnh của thuật toán.")

if __name__ == "__main__":
    run_statistical_analysis(30)
