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

### 💡 Ý tưởng cốt lõi (Lấy cảm hứng từ đâu?)
Thuật toán bắt chước cách cơ thể con người phản ứng khi bị nhiễm bệnh:
* Khi có virus (Bài toán khó) xâm nhập, cơ thể tạo ra rất nhiều **Kháng thể** (Các phương án giải quyết ngẫu nhiên). 
* Cơ thể sẽ đánh giá xem kháng thể nào diệt virus tốt nhất (Độ thích nghi/Fitness cao). 
* Kháng thể tốt đó sẽ được giữ lại, **nhân bản (Cloning)** ra rất nhiều bản sao. Trong quá trình nhân bản, có xảy ra sự **đột biến (Mutation)** ngẫu nhiên để dò dẫm, tạo ra các thế hệ kháng thể sau xịn hơn thế hệ trước.

### ⚙️ Áp dụng vào Máy tính (Tối ưu hóa Toán học)
Trong máy tính, chúng ta không có virus thật, mà thay vào đó là **Bài toán Tối ưu hóa**.
* Bạn hãy tưởng tượng mình đang đứng trên một dãy núi khổng lồ, sương mù mù mịt. Nhiệm vụ của bạn là phải tìm ra **thung lũng thấp nhất** (Giá trị Min của hàm số toán học Sphere hoặc Rastrigin).
* Thuật toán sẽ thả ngẫu nhiên 100 người lính (100 kháng thể) xuống dãy núi. Nó sẽ chọn ra những người đang đứng ở vị trí thấp nhất, nhân bản họ lên, và cho họ bước ngẫu nhiên (đột biến) để dò đường tiếp. 
* Cứ lặp đi lặp lại 100-500 vòng lặp (Thế hệ/Generations), đội quân của bạn chắc chắn sẽ "đổ dồn" về đúng cái đáy thấp nhất của dãy núi.

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