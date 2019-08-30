#!python3.5
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#open browser
driver = webdriver.Opera()
web = driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
#time wait because load page
time.sleep(4)
#operation for write username
input_username_XP = "//input[@name='username']"

input_username = driver.find_element_by_xpath(input_username_XP)

(ActionChains(driver)
    .move_to_element(input_username)
    .click()
    .send_keys('')#name user
    .perform())

#time wait for security
time.sleep(3)
#operation for write password
input_password_XP = "//input[@name='password']"

input_password = driver.find_element_by_xpath(input_password_XP)

(ActionChains(driver)
    .move_to_element(input_password)
    .click()
    .send_keys('')#password user
    .send_keys(Keys.ENTER)
    .perform())
#time wait for load page
driver.implicitly_wait(15)
#remove span on window
for x in range(5):
    try:
        span_tela = driver.find_element_by_xpath('/html/body/div[%d]/div'%x)
        span_button = driver.find_element_by_xpath('/html/body/div[%d]/div/div/div[3]/button[2]'%(x))
        (ActionChains(driver)
            .move_to_element(span_button)
            .click()
            .perform())

#time wait for load page
    except:
        print('not is necessary','/html/body/div[%d]/div'%x,'/html/body/div[%d]/div/div/div[3]/button[2]'%(x))
        pass

#operation for like determine number of main page
for x in range(4):
    like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/article[%x]/div[2]/section[1]/span[1]/button'%(x+1))
    (ActionChains(driver)
        .move_to_element(like_button)
        .click()
        .perform())
    if x == 3:
        for x in range(3,9):
            like_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[1]/div/article[%x]/div[2]/section[1]/span[1]/button'%(x+1))
            (ActionChains(driver)
                .move_to_element(like_button)
                .click()
                .perform())
            
            ''' 
try:
    
    web = driver.get("https://www.instagram.com/explore/tags/barradaestiva/")
    l=1
    c=1
    for x in range(7):
        l+= 1
        buttonPage = driver.find_element_by_xpath('*[@id="react-root"]/section/main/article/div[1]/div/div/div[%d]/div[%d]/a/div/div[2]'%(c,l))
        (ActionChains(driver)
             .move_to_element(buttonPage)
             .click()
             .perform())
        buttonCurtir = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button') 
        (ActionChains(driver)
             .move_to_element(buttonPage)
             .click()
             .perform())
        buttonExit = driver.find_element_by_xpath('/html/body/div[3]/button[1]')
        (ActionChains(driver)
             .move_to_element(buttonPage)
             .click()
             .perform())
        if l == 3:
            c+=1
            l=1
    
except:
    print('fail')'''
