from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from local_var_funcs import (
	user_info_exporter,
	user_info_getter, 
)


user_info_exporter(
	username='thisistestingselenium@gmail.com',
	password='passwd@2',
)
user_username, user_password = user_info_getter('USERNAME', 'PASSWORD')

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

username = browser.find_element(by=By.NAME, value='username')
username.send_keys(user_username)

password = browser.find_element(by=By.NAME, value='password')
password.send_keys(user_password)

submit_btn = browser.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
