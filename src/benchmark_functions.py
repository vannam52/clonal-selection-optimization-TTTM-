import numpy as np

def sphere(x):
    """
    Hàm Sphere: f(x) = sum(x_i^2)
    Bài toán tìm Min, giá trị tối ưu bằng 0 tại x = [0, 0, ..., 0]
    """
    return np.sum(x**2)

def rastrigin(x, A=10):
    """
    Hàm Rastrigin: f(x) = A*n + sum(x_i^2 - A*cos(2*pi*x_i))
    Bài toán tìm Min, giá trị tối ưu bằng 0 tại x = [0, 0, ..., 0]
    """
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))
