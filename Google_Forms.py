from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get('https://forms.gle/dHdyrY6tb3JDfsPPA')
driver.find_element(by='xpath', value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('Md. Hasibur Rahman')
driver.find_element(by='xpath', value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('2010977137')
driver.find_element(by='xpath', value='//div[@role="button"]').click()

driver.quit()