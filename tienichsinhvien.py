import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
driver = webdriver.Chrome()
driver.get('https://tienichsv.ou.edu.vn/#/home')
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//span[text()='Đăng nhập tài khoản HCMCOU-SSO']").click()
time.sleep(5)
tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.get('https://id.ou.edu.vn/auth/login')
time.sleep(5)
userType = Select(driver.find_element(By.ID, 'form-usertype'))
userType.select_by_index(0)
with open('studentInfor.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']
(driver.find_element(By.NAME, 'form-username')).send_keys(user)
(driver.find_element(By.NAME, 'form-password')).send_keys(password)
driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()
time.sleep(5)
driver.switch_to.window(tabs[0])
driver.close()
driver.switch_to.window(tabs[1])
driver.find_element(By.XPATH, "//*[@id='navbarNav']/ul/li[2]/a").click()
time.sleep(5)
divThongTin = driver.find_element(By.CSS_SELECTOR,
                                  "body > app-root > div > div > div > div.contentshow.ng-star-inserted > div > div "
                                  "> div.px-md-0.frame_left > app-userinfo > div > div.card-body.py-0 > div > div > "
                                  "div.col-md-10.px-1 > div:nth-child(1) > div.card-body.py-1 > div")
divThongTin = divThongTin.get_attribute('innerText')
print(divThongTin)
driver.close()
