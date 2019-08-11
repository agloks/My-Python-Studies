import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r"C:\Users\x\Desktop\chromedriver.exe")
web = driver.get("https:...")

choice = 3
time.sleep(3)

for x in range(choice):
    #xpath in /div and /article is changed sometime because instagram changed values
    like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article[%d]/div[2]/section[1]/span[1]/button'%(x+1))
    (ActionChains(driver)
         .move_to_element(like_button)
         .click()
         .perform())
