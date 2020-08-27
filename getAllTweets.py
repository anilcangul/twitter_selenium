from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://twitter.com/")

time.sleep(3)

kullanici_adi = "sami1234"
sifre = "124325345"
time.sleep(3)

driver.close()
