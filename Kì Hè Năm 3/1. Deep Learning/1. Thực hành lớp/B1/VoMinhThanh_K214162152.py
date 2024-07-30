# # - Import Lib
# import json
# import requests

# # - Load data
# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)
# json_string = json.dumps(response.json(), indent = 3)
# with open('users.json', "w") as outfile:
#     outfile.write(json_string)


# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://www.24h.com.vn/'
# response = requests.get(url)
# return_data = response.text

# if response. status_code == 200:
#     soup = bs(response.content, 'html.parser')
#     cm = soup.find('div', class_='boxDoiSong')
#     print(cm)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_experimental_option("prefs", {
#         "download.default_directory": "C:/Users/DELL/Downloads",
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
#     })
# Khởi tạo WebDriver cho Chrome
#driver_path = r"D:\GitHub\UEL-Course\Kì Hè Năm 3\1. Deep Learning\chrome-win64\chrome-win64\chrome.exe"
driver = webdriver.Chrome()

# URL của trang web cần tương tác
url = "https://ls.cafef.vn/du-lieu.chn"
driver.get(url)

# Tìm và click vào nút để mở ra lịch sử dữ liệu
btn_lichsudulieu = driver.find_element(By.XPATH, '//*[@id="pagewrap"]/div[1]/div[1]/div[2]/a[3]')
btn_lichsudulieu.click()

# Tìm ô nhập tìm kiếm, gửi từ khóa 'Techcombank'
input_search = driver.find_element(By.ID, "ContentPlaceHolder1_ctl00_acp_inp_disclosure")
input_search.send_keys("Techcombank")

# Nhấn ENTER để tìm kiếm
input_search.send_keys(Keys.RETURN)

# Nhập khoảng thời gian cần tìm kiếm
input_time = driver.find_element(By.ID, "date-inp-disclosure")
input_time.send_keys("01/01/2023 - 31/12/2023")

# Tìm và click vào nút tìm kiếm dữ liệu
btn_xem = driver.find_element(By.ID, "owner-find")
btn_xem.click()

# Tìm phần tử bảng dữ liệu
tbl_data = driver.find_element(By.ID, "owner-contents-table")

# Tìm tất cả các hàng trong bảng
all_rows = tbl_data.find_elements(By.TAG_NAME, "tr")

# Lặp qua từng hàng và in ra nội dung của nó
for row in all_rows:
    print(row.text)
    sleep(1)  # Dừng 1 giây giữa mỗi hàng để dễ theo dõi

# Tìm và click vào nút 'Next' để chuyển sang trang tiếp theo của bảng
btn_next = driver.find_element(By.XPATH, '//*[@id="divStart"]/div/div[3]/div[3]')
btn_next.click()

# Đóng WebDriver
driver.quit()
