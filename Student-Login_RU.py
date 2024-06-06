# import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Input ID & Pass
id = input("Student ID  : ")
from getpass import getpass
pas = getpass("Password : ")
# Headless Means Chrome open hobe na
options = Options()
options.add_argument('headless')
# webbrowser
driver = webdriver.Chrome(options=options)
driver.get('http://rurfid.ru.ac.bd/ru_services/public/login')
driver.find_element(by='name', value='username').send_keys(id)
driver.find_element(by='name', value='password').send_keys(pas)
driver.find_element(by='xpath', value='//button[@type="submit"]').click()
driver.find_element(by='xpath', value='//a[@class="btn btn-vermillion col-sm-2"]').click()
links = []
number_of_links = driver.find_elements(by='xpath', value='//td[@class="text-right"]')
for i in number_of_links:
    link = i.find_element(by='xpath', value='./a').get_attribute('href')
    links.append(link)
# Genarate date time for file name
from datetime import datetime
now = datetime.now()
date_time = now.strftime('%d-%b-%Y-%H-%M-%S')

# File create and store
import pandas as pd
my_data_frame = pd.DataFrame({'Download Form Link':links})
my_data_frame.to_csv(f""+id+"--"+date_time+".csv")

driver.quit()