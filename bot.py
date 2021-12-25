from selenium import webdriver
import requests
import time

driver = webdriver.Edge()

driver.maximize_window()

x = requests.get('https://randomuser.me/api')
userdata = x.json()

name = userdata['results'][0]['name']
login = userdata['results'][0]['login']


driver.get('https://tinyurl.com/gmailsigninforbot')

driver.find_element_by_name("firstName").send_keys(name['first'])

time.sleep(1)

driver.find_element_by_name("lastName").send_keys(name['last'])

time.sleep(1)

strline = 'fkdsafue03wofdsiuflidsjlijdisfsdffofdsiuflidsjlijdisfsdff'

# driver.find_elements_by_id("username").send_keys("fjdadslkdadsjfldskdsf")

time.sleep(1)

driver.find_element_by_name("Passwd").send_keys("afdfsdfds")

time.sleep(1)

driver.find_element_by_name("ConfirmPasswd").send_keys("fdafs")

time.sleep(1)




