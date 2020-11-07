from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="/Users/username/Desktop/chromedriver")
for x in range(4):
    driver.get("https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem")
    sleep(1)
    driver.find_element_by_xpath("//input[@name=\"mli\"]").send_keys("your username")
    sleep(4)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys("your password.")
    sleep(4)
    driver.find_element_by_name('dologin').click()
    sleep(4)
    driver.find_element_by_xpath(
        "//select[@name='5.5.1.27.1.11.0']/option[text()='FALL/WINTER 2020-2021 UNDERGRADUATE "
        "STUDENTS']").click()
    sleep(4)
    driver.find_element_by_name('5.5.1.27.1.13').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.1.23').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.7.7').send_keys("the class code")
    sleep(4)
    driver.find_element_by_name('5.1.27.7.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.11.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.27.27.9').click()
    sleep(4)
    driver.find_element_by_name('5.1.3.1.1').click()
    sleep(4)
    driver.close()
    sleep(1800)
