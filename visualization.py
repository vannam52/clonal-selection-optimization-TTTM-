import matplotlib.pyplot as plt
import seaborn as sns

def plot_convergence(cs_history, ga_history=None):
    """
    Vẽ đồ thị so sánh tốc độ hội tụ (fitness qua các thế hệ).
    (Nhiệm vụ của Người số 4)
    """
    # Kích hoạt giao diện xịn xò của seaborn
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10, 6))
    
    # Dùng seaborn để vẽ đường cho Clonal Selection
    sns.lineplot(data=cs_history, label="Clonal Selection (Hệ miễn dịch)", color="blue", linewidth=2.5)
    
    # Dùng seaborn để vẽ đường cho Genetic Algorithm
    if ga_history is not None:
        sns.lineplot(data=ga_history, label="Genetic Algorithm (Di truyền)", color="orange", linewidth=2.5, linestyle="--")
    
    plt.title("So sánh tốc độ tìm nghiệm: Clonal Selection vs Genetic Algorithm", fontsize=15, fontweight="bold")
    plt.xlabel("Thế hệ tiến hóa (Generations)", fontsize=12)
    plt.ylabel("Giá trị hàm mục tiêu (Fitness - Càng gần 0 càng tốt)", fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()
