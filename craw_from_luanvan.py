import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.set_window_size(920, 1200)
action = ActionChains(driver)
'''
CRAWL PDF FROM luanvan.net.vn
'''

driver.get('https://luanvan.net.vn/luan-van/bat-dong-san/?page=1')
documents = driver.find_element(By.XPATH, '//*[@id="documents"]/div[2]/ul')
links = documents.find_elements(By.CLASS_NAME, 'title')
links = [link.get_attribute('href') for link in links]
for link in links:
    driver.get(link)
    document_iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.get(document_iframe.get_attribute('src'))
    time.sleep(2) # wait to load all images
    action.send_keys(Keys.HOME)
    button_to_click = driver.find_element(By.ID, 'next')
    num_pages = driver.find_element(By.ID, 'numPages').text
    num_pages = int(num_pages[3:])
    print(num_pages)
    for i in range(num_pages):
        action.click(button_to_click)
        action.perform()
        driver.save_screenshot(f'crawled_image/screenshot_{time.time()}.png')

