import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.set_window_size(1920, 980)

'''
CRAWL PDF FROM ALLDATASHEET
'''

#first page to find all links
driver.get('https://www.alldatasheet.com/view.jsp?Searchword=HL')
elems = driver.find_elements(By.XPATH, "//a[@href]")
pdf_links = []
preview_links = []
for elem in elems:
    link = elem.get_attribute("href")
    if 'datasheet-pdf/pdf' in link:
        # link = link.replace('/pdf/', '/download/')
        preview_links.append(link)
        link = link.replace('/pdf/', '/view/')
        pdf_links.append(link)

# download pdf by click in button
for link_1, link_2 in zip(preview_links, pdf_links):
    time.sleep(2) # too fast of loading a web from server will cause crash
    driver.get(link_1)
    time.sleep(2)
    driver.get(link_2)
    # code = driver.find_element(By.XPATH, '/html/body/div[5]/table/tbody/tr/td/form/table/tbody/tr[1]').text
    # code = re.sub("[:a-zA-Z\s]+", '', code)
    # driver.find_element(By.XPATH, '/html/body/div[5]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input').send_keys(code)
    # driver.find_element(By.XPATH, '/html/body/div[5]/table/tbody/tr/td/form/table/tbody/tr[3]/td/input[2]').submit()

    #--------------------------OR---------------------
    driver.switch_to.frame('333')
    driver.find_element(By.ID, 'download').click()


input("nhap bat ki de dong: ") # get from keyborad
driver.quit()

