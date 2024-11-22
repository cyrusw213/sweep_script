
from selenium.webdriver.firefox.service import Service
import selenium
import time, re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import uniform

email = ''
URL = ''

#driver set up
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service)

#open URL 
driver.get(URL)
get_URL_source = driver.page_source

url_ngxFrame = re.findall("ngxFrame\d\w+", get_URL_source)[0]

time.sleep(20+round(uniform(0, 5),2))
driver.switch_to.frame(driver.find_element(By.ID, url_ngxFrame))

#add email
email_input = driver.find_element(By.ID, "xReturningUserEmail")
time.sleep(4+round(uniform(0, 5),2))
email_input.send_keys(email)

#click button
time.sleep(5+round(uniform(0, 5),2))
driver.find_element(By.XPATH, """//*[@id="xCheckUser"]/span""").click()
time.sleep(20+round(uniform(0, 5),2))


#click submit on second page
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.ID, url_ngxFrame))
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/div/div/div/div/form[2]/div[3]/div/div[1]/a[2]").click()


# driver.find_element(By.XPATH, """//*[@id="multioptin_0_Secondary"]""").click()
time.sleep(5+round(uniform(0, 5),2))
driver.find_element(By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/div/div/div/div/form[2]/div[3]/div/div[2]/button").click()


action = ActionChains(driver)
action.send_keys(Keys.TAB)
action.send_keys(Keys.ENTER)
action.perform()
time.sleep(10+round(uniform(0, 5),2))


#close browser
driver.quit()

