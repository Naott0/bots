import time
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")


def get_data(url):
    try:

        driver = webdriver.Chrome(executable_path='/selenium/chromedriver',
                                  options=options)
        driver.get(url=url)
        time.sleep(10)
        button2 = driver.find_element(By.XPATH, value='//*[@id="bannerLine_close"]')
        button2.click()
        button3 = driver.find_element(By.XPATH,
                                      value='/html/body/div[1]/div[4]/div[1]/div[2]/div/div[2]/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/a/div/div[2]/div[2]/div/div/div[1]')
        button3.click()
        print("Голос есть !")

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input("Введи число лайков: "))
    url = input("URL: ")
    url_list = [url] * process_count
    print(url_list)
    p = Pool(processes=process_count)
    print(process_count)
    p.map(get_data, url_list)
