import selenium
from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://mlwbd.com/')
time.sleep(5)
driver.find_element(by='xpath', value='//nav[@class="navbar navbar-expand-md navbar-dark navbar-custom fixed-top"]/a').click()
time.sleep(15)

contents = driver.find_elements(by='xpath', value='//div[@class="poster"]')

links = []

for it in contents:
    link = it.find_element(by='xpath', value='//div[@class="poster"]/a').get_attribute("href")
    links.append(link)

my_disk = {'Movie links':links}

allLinks = pd.DataFrame(my_disk)
allLinks.to_markdown('allLinks.md')

driver.quit()