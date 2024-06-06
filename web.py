
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://www.facebook.com/r.php?r=101')

time.sleep(3)
driver.find_element(By.NAME, "firstname").send_keys("Hasibur")
time.sleep(3)
driver.find_element(By.NAME, "lastname").send_keys("Rahman")
time.sleep(3)
driver.find_element(By.NAME, "reg_email__").send_keys("rubwhy672@fuwamofu.com")
time.sleep(3)
driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("rubwhy672@fuwamofu.com")
time.sleep(3)
driver.find_element(By.NAME, "reg_passwd__").send_keys("#&35.Ha$ib")
time.sleep(3)

date = driver.find_element(By.XPATH, "//select[@id='year']").send_keys("1996")
time.sleep(5)
driver.find_element(By.NAME, "sex").click()
time.sleep(3)
driver.find_element(By.NAME, "websubmit").click()
time.sleep(30)



