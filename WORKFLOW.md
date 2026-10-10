# 🗺️ QUY TRÌNH THỰC HIỆN ĐỒ ÁN CLONAL SELECTION (MASTER PLAN)

Dưới đây là lộ trình chi tiết để nhóm 4 người cùng làm việc một cách hiệu quả, tránh conflict code và hoàn thành đúng tiến độ.

---

## 🟢 GIAI ĐOẠN 1: KHỞI TẠO & MÔI TRƯỜNG (Cả nhóm)

**1. Quản lý source code (Git/GitHub):**
- Mọi người `git clone` kho lưu trữ về máy.
- Tạo và làm việc trên branch riêng (VD: `git checkout -b task-nhanban`).
- Tuyệt đối không đẩy code đè lên branch `main` khi chưa họp nhóm.

**2. Cài đặt thư viện (Bắt buộc):**
Tất cả thành viên mở Terminal và chạy lệnh sau để đảm bảo môi trường giống nhau:
```bash
pip install -r requirements.txt
```

---

## 🟡 GIAI ĐOẠN 2: BẮT TAY VÀO CODE (Phân công nhiệm vụ)

Đây là lúc thay thế các dòng code "giả lập" (mock) bằng code toán học thật.

### 🧑‍💻 Bước 1: Khởi tạo dữ liệu (Người số 1)
- **Nơi làm việc:** `benchmark_functions.py` và hàm `init_population` trong `clonal_selection.py`.
- **Nhiệm vụ:**
  - Viết code dùng `numpy` tạo ra quần thể ngẫu nhiên ban đầu (VD: ma trận 100 kháng thể, mỗi cái có 5 chiều không gian).
  - Viết hàm đánh giá Fitness dựa trên hàm mục tiêu Sphere/Rastrigin.

### 🧑‍💻 Bước 2: Lập trình lõi thuật toán (Người số 2)
- **Nơi làm việc:** Hàm `clone` và `mutate` trong `clonal_selection.py`.
- **Nhiệm vụ:** 
  - **Clone:** Viết công thức nhân bản (Kháng thể giỏi nhân nhiều bản sao, kháng thể dở nhân ít).
  - **Mutate:** Viết công thức đột biến (Cộng số ngẫu nhiên nhỏ vào bản sao của kháng thể giỏi, cộng số ngẫu nhiên lớn vào bản sao của kháng thể dở).

### 🧑‍💻 Bước 3: Thuật toán đối trọng GA (Người số 3)
- **Nơi làm việc:** `ga_comparison.py`.
- **Nhiệm vụ:** Tìm hiểu và dùng thư viện `PyGAD` (Thuật toán Di truyền - Genetic Algorithm). Truyền bài toán Sphere vào cho thư viện chạy tự động, sau đó trả về mảng lịch sử Fitness qua từng thế hệ để đem đi so sánh.

---

## 🔴 GIAI ĐOẠN 3: LẮP RÁP, CHẠY THỬ & BÁO CÁO

### 🧑‍💻 Bước 4: Lắp ráp vào luồng chính (Người 1 + 2)
- **Nơi làm việc:** Vòng lặp `for` trong file `main.py`.
- **Nhiệm vụ:** Ráp tuần tự các hàm từ Bước 1 và 2 vào vòng lặp tiến hóa (VD: 200 vòng). Lưu điểm Fitness tốt nhất của mỗi vòng vào mảng `cs_fitness_history`.

### 🧑‍💻 Bước 5: Chạy thử & "Độ" tham số (Cả nhóm)
- Chạy lệnh `python main.py` ở Terminal.
- Cùng nhau thử nghiệm thay đổi các thông số (Pop Size = 500, Iterations = 500, Tỷ lệ đột biến...) để ép thuật toán tìm ra kết quả tiệm cận số 0 nhanh và mượt nhất có thể.

### 🧑‍💻 Bước 6: Trực quan hóa & Thuyết trình (Người số 4)
- **Nơi làm việc:** `visualization.py` và File Báo cáo (Word/PowerPoint).
- **Nhiệm vụ:** Chỉnh sửa code vẽ biểu đồ (màu sắc, chú thích) cho chuyên nghiệp. Tổng hợp lý thuyết, copy biểu đồ kết quả đưa vào Slide báo cáo. 
- Merge (gộp) code từ các nhánh riêng của mọi người vào nhánh `main` và kết thúc dự án.

---
**💡 Châm ngôn nhóm:** 
> *Code trên nhánh riêng, test kỹ trước khi gộp, và nhớ chụp lại cái biểu đồ xịn nhất để đi báo cáo!*
