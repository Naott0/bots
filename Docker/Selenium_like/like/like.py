import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
x = 0
for i in range(1, 1000):
    t = random.randint(60,180)
    driver = webdriver.Chrome(executable_path='/selenium/chromedriver')
    driver.get('https://www.rostov.kp.ru/media/930213/')
    time.sleep(2)
    button2 = driver.find_element(By.XPATH, value='//*[@id="bannerLine_close"]')
    button2.click()
    button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[3]/div[3]/div/a/div/div[2]/div[2]/div/div/div[1]')
    button.click()
    print("Голос за Марина Лементова!", x)
    button3 = driver.find_element(By.XPATH, value='/html/body/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/a/div/div[2]/div[2]/div/div/div[1]')
    button3.click()
    print("Голос за Елена Навериани!", x)
    x = x+1
    print("TIMER",t)
    time.sleep(t)
    driver.quit()