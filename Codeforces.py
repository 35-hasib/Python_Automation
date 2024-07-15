
# print('''Make sure turn on "Hide solved problems from problemset" in Codeforces account. And make more friends...''')

# name = input("Handle/Email : ")
# from getpass import getpass
# pas = getpass("Password : ")

name = 'Hasibur_Rahman'
pas = '#&35.Ha$ib'


import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


i = 0

while True:
    
    try:
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get('https://codeforces.com/enter?back=%2F')
        time.sleep(2)
        driver.find_element(By.NAME, "handleOrEmail").send_keys(name)
        driver.find_element(By.NAME, "password").send_keys(pas)
        driver.find_element(by='xpath', value='//tbody/tr[4]/td[1]/div[1]/input[1]').click()
        time.sleep(2)
        driver.find_element(by='xpath', value='''//a[contains(text(),'Problemset')]''').click()
        time.sleep(2)
        driver.find_element(By.NAME, "minDifficulty").send_keys('800')
        driver.find_element(By.NAME, "maxDifficulty").send_keys('800')

        driver.find_element(by='xpath', value='''//body/div[@id='body']/div[4]/div[1]/div[2]/div[3]/form[1]/div[4]/input[1]''').click()
        time.sleep(2)
        driver.find_element(by='xpath', value='''//tbody/tr[2]/td[5]''').click()
        time.sleep(3)
        driver.find_element(by='xpath', value='''//body/div[@id='body']/div[4]/div[2]/div[3]/form[1]/label[1]/input[1]''').click()
        time.sleep(2)

        driver.find_element(by='xpath', value='''//tbody/tr[2]/td[1]''').click()
        time.sleep(2)

        driver.find_element(by='xpath', value='''//span[@id='program-source-text-copy']''').click()
        time.sleep(2)
        driver.find_element(by='xpath', value='''//body/div[@id='facebox']/div[1]/a[1]''').click()
        time.sleep(2)

        driver.find_element(by='xpath', value='''//a[contains(text(),'Problemset')]''').click()
        time.sleep(2)
        driver.find_element(By.NAME, "minDifficulty").send_keys('800')
        driver.find_element(By.NAME, "maxDifficulty").send_keys('800')

        driver.find_element(by='xpath', value='''//body/div[@id='body']/div[4]/div[1]/div[2]/div[3]/form[1]/div[4]/input[1]''').click()
        time.sleep(2)
        driver.find_element(by='xpath', value='''//tbody/tr[2]/td[2]/div[1]''').click()
        time.sleep(2)
        driver.find_element(by='xpath', value='''//a[contains(text(),'Submit')]''').click()
        time.sleep(3)

        driver.find_element(by='xpath', value='''//tbody/tr[4]/td[2]/div[1]/div[2]''').click()
        time.sleep(2)

        act = ActionChains(driver)
        act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(2)

        driver.find_element(by='xpath', value='''//input[@id='singlePageSubmitButton']''').click()
        time.sleep(5)
        
        print("Mission completed....!")
        driver.close();
        i = i+1
    except:
        print("An Error Found ....!")
    if i == 1:
        break

        
