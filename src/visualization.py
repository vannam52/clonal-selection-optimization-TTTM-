import matplotlib.pyplot as plt

def plot_convergence(cs_history, ga_history=None, func_name="Benchmark"):
    """
    Vẽ đồ thị so sánh bằng Matplotlib theo yêu cầu của đề tài.
    """
    plt.figure(figsize=(10, 6))
    
    # Đường Clonal Selection
    plt.plot(cs_history, label='Clonal Selection (Hệ miễn dịch)', color='blue', linewidth=2)
    
    # Đường Genetic Algorithm
    if ga_history is not None:
        plt.plot(ga_history, label='Genetic Algorithm (Di truyền)', color='orange', linestyle='--', linewidth=2)
    
    plt.title(f"So sánh tốc độ hội tụ: CS vs GA (Bài toán: {func_name})", fontsize=16)
    plt.xlabel("Thế hệ tiến hóa (Iterations)", fontsize=12)
    plt.ylabel("Giá trị Fitness (Càng gần 0 càng tốt)", fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend(loc='upper right', fontsize=12)
    
    # Lưu ảnh hoặc hiển thị
    plt.tight_layout()
    plt.show()
