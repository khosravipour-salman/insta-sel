from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
	

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

username = browser.find_element(by=By.NAME, value='username')
username.send_keys('thisistestingselenium@gmail.com')

password = browser.find_element(by=By.NAME, value='password')
password.send_keys('passwd@2')

submit_btn = browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
