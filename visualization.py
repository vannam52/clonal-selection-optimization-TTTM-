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
    
    # TODO: Dùng plt.plot để vẽ đường cho Clonal Selection
    
    # TODO: Dùng plt.plot để vẽ đường cho Genetic Algorithm (Nếu có)
    
    plt.title("So sánh sự hội tụ: Clonal Selection vs Genetic Algorithm", fontsize=14)
    plt.xlabel("Thế hệ (Generations)", fontsize=12)
    plt.ylabel("Độ thích nghi (Fitness - Càng thấp càng tốt)", fontsize=12)
    plt.legend()
    plt.show()
