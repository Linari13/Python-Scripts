"""
    Creatd by: Frédéric Peña
    on the: 27/03/2020
"""

from selenium import webdriver

driver = webdriver.Firefox() #We set the webdriver to Firefox
driver.get("https://s1.demo.opensourcecms.com/s/44")

print(driver.title)      #checking we land on the correct webpage

driver.switch_to_frame("preview-frame")                              #We make sure to be on the correct frame as page contains 2

inputElement = driver.find_element_by_name("txtUsername")            #finding username input element
inputElement.send_keys("opensourcecms")                              #Sending username input

inputElement = driver.find_element_by_name("txtPassword")            #finding password input element
inputElement.send_keys("opensourcecms")                              #Sending password input

inputElement.submit()

driver.quit()
