<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />
  <img src="https://img.shields.io/badge/PyGAD-4B8BBE?style=for-the-badge&logo=python&logoColor=white" alt="PyGAD" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge&logo=python&logoColor=white" alt="Seaborn" />
  <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter" />
  <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252" alt="Google Colab" />
</p>

# Clonal Selection Algorithm for Function Optimization

## 📝 Giới thiệu đề tài
Đề tài áp dụng **Thuật toán lựa chọn dòng vô tính (Clonal Selection Algorithm)** để giải quyết bài toán tối ưu hóa (tìm Min/Max) trên các hàm chuẩn (benchmark functions) như hàm **Sphere** và **Rastrigin**.

Mục tiêu là mô phỏng lại cách hoạt động của hệ miễn dịch nhân tạo (Artificial Immune System) thông qua quá trình lựa chọn, nhân bản và đột biến các kháng thể.

## 🚀 Các công cụ sử dụng
- **Ngôn ngữ:** Python
- **Thư viện Thuật toán:** NumPy, PyGAD (so sánh GA)
- **Thư viện Trực quan hóa:** Matplotlib, Seaborn, tqdm
- **Môi trường:** Jupyter Notebook / Google Colab

## 📂 Cấu trúc thư mục
- `benchmark_functions.py`: Chứa các hàm toán học cần tối ưu (Sphere, Rastrigin).
- `main.py`: File code chính chứa khung thuật toán.
- `requirements.txt`: Danh sách các thư viện cần thiết.

## 🛠️ Hướng dẫn cài đặt
1. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt
   ```
2. Chạy file chính:
   ```bash
   python main.py
   ```