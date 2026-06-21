import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo Trình duyệt Chrome mở toàn màn hình
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    # =========================================================================
    # TEST CASE 1: ĐĂNG NHẬP THÀNH CÔNG (LOGIN SUCCESS)
    # =========================================================================
    print("--- Đang chạy TC1: Đăng nhập thành công ---")
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Điền Username và Password chuẩn của trang
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    
    # Click nút Login
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].click();", login_btn)
    
    # Kiểm tra thông báo thành công
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "You logged into a secure area!" in flash_msg.text
    print("=> TC1: PASSED")
    time.sleep(1.5)

    # =========================================================================
    # TEST CASE 2: ĐĂNG XUẤT HỆ THỐNG (LOGOUT)
    # =========================================================================
    print("\n--- Đang chạy TC2: Đăng xuất ---")
    # Click nút Logout
    logout_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.secondary.radius")))
    driver.execute_script("arguments[0].click();", logout_btn)
    
    # Kiểm tra xem đã quay về trang đăng nhập chưa
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "You logged out of the secure area!" in flash_msg.text
    print("=> TC2: PASSED")
    time.sleep(1.5)

    # =========================================================================
    # TEST CASE 3: ĐĂNG NHẬP THẤT BẠI (LOGIN FAILED)
    # =========================================================================
    print("\n--- Đang chạy TC3: Đăng nhập sai tài khoản ---")
    # Nhập sai tài khoản
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("sai_tai_khoan")
    driver.find_element(By.ID, "password").send_keys("sai_mat_khau")
    
    # Click nút Login
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].click();", login_btn)
    
    # Kiểm tra xem có hiện thông báo lỗi màu đỏ không
    flash_msg = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your username is invalid!" in flash_msg.text
    print("=> TC3: PASSED")
    time.sleep(1.5)

except Exception as e:
    print(f"\n[LỖI] Test Case thất bại! Chi tiết: {e}")

finally:
    print("\nĐang đóng trình duyệt...")
    driver.quit()