import numpy as np

def init_population(pop_size, dim, bounds):
    """
    Khởi tạo quần thể kháng thể ngẫu nhiên.
    (Nhiệm vụ của Người số 1)
    """
    pass

def evaluate_fitness(population, fitness_func):
    """
    Đánh giá độ thích nghi (affinity) của từng kháng thể.
    """
    pass

def clone(population, fitness, clone_rate):
    """
    Nhân bản các kháng thể tốt. Tỷ lệ nhân bản tỷ lệ thuận với fitness.
    (Nhiệm vụ của Người số 2)
    """
    pass

def mutate(clones, mutation_rate):
    """
    Đột biến các bản sao. Tỷ lệ đột biến tỷ lệ nghịch với fitness.
    (Nhiệm vụ của Người số 2)
    """
    pass

def select(population, clones, pop_size):
    """
    Chọn lọc các kháng thể tốt nhất cho thế hệ tiếp theo.
    """
    pass
