# BÁO CÁO BÀI TẬP: KIỂM THỬ TỰ ĐỘNG VỚI SELENIUM

## 1. Thông Tin Sinh Viên
* **Họ và tên:** Vương Xuân Giáp
* **Mã sinh viên:** 23010564
* **Môn học:** Đảm bảo chất lượng và Kiểm thử phần mềm

## 2. Kịch Bản Kiểm Thử (Test Cases)
Bài tập thực hiện kiểm thử tự động trên website: `https://the-internet.herokuapp.com/login`

| Mã TC | Tên Chức Năng | Các Bước Thực Hiện | Kết Quả Mong Đợi | Trạng Thái |
| :--- | :--- | :--- | :--- | :--- |
| **TC01** | Đăng nhập thành công | 1. Vào trang Login.<br>2. Nhập username `tomsmith` và password chuẩn.<br>3. Click "Login". | Đăng nhập thành công, hiển thị thông báo "You logged into a secure area!". | **PASSED** |
| **TC02** | Đăng xuất hệ thống | 1. Tại trang Secure Area, click nút "Logout". | Đăng xuất thành công, chuyển về trang Login và báo "You logged out...". | **PASSED** |
| **TC03** | Đăng nhập thất bại | 1. Nhập sai username hoặc password.<br>2. Click "Login". | Đăng nhập thất bại, hiển thị thông báo lỗi màu đỏ "Your username is invalid!". | **PASSED** |

## 3. Công Cụ Sử Dụng
* **Ngôn ngữ:** Python 3.13
* **Thư viện:** `selenium` (Phiên bản 4)
* **Trình duyệt điều khiển:** Google Chrome

## 4. Hướng Dẫn Chạy Mã Nguồn
1. Clone repository này về máy.
2. Cài đặt thư viện: `pip install selenium`
3. Chạy file test: `python Lab9.py`
