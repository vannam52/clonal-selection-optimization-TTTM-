import numpy as np

def run_ga(fitness_func=None, num_generations=200):
    """
    (BẢN MOCK DEMO) Chạy thuật toán Di truyền bằng thư viện PyGAD để so sánh.
    (Nhiệm vụ của Người số 3)
    """
    print("  -> Đang thiết lập nhiễm sắc thể cho GA...")
    print("  -> Đang tiến hóa qua các thế hệ (Genetic Algorithm)...")
    
    # Tạo data giả (mock data) thể hiện sự hội tụ của thuật toán GA
    # Giả sử GA hội tụ chậm hơn Clonal Selection một chút
    ga_history = 500 * np.exp(-0.015 * np.arange(num_generations)) + np.random.normal(0, 3, num_generations)
    ga_history = np.maximum(ga_history, 0) # Không cho âm
    
    return ga_history.tolist()
