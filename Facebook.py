from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.fb.com/')

driver.find_element(by='xpath', value='//*[@id="email"]').send_keys('hrrahman355555@gmail.com')
driver.find_element(by='xpath', value='//*[@id="pass"]').send_keys('#&35.Ha$ib')
driver.find_element(by='name', value='login').click()
time.sleep(10)
driver.find_element(by='xpath', value='//a[@aria-label="Friends"]').click()
time.sleep(5)
driver.find_element(by='xpath', value='//a[@href="/friends/list/"]').click()
time.sleep(2)
driver.find_element(by='xpath', value='//input[@aria-label="Search bar for friend search"]').send_keys('Abir Hasan')
time.sleep(2)
driver.find_element(by='xpath', value='//a[@href="https://www.facebook.com/profile.php?id=100047944209883"]').click()
time.sleep(15)
for i in range(10):
    driver.find_element(by='xpath', value='//div[@aria-label="Like"]').click()
    time.sleep(2)