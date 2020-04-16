"""
    Creatd by: Frédéric Peña
    on the: 27/03/2020
"""

from selenium import webdriver

driver = webdriver.Firefox()                                    #We set the webdriver to Firefox
driver.get("https://www.WebSiteAddress")                        #we go on the website login page

print(driver.title)                                             #checking we land on the correct webpage

""" driver.switch_to_frame("body-inner") """                           #We switch to the correct frame IF NEEDED

inputElement = driver.find_element_by_name("Username element name")    #finding username input element
inputElement.send_keys("User name to enter")                           #Sending username input

inputElement = driver.find_element_by_name("password element name")    #finding password input element
inputElement.send_keys("Password to enter")                            #Sending password input

inputElement.submit()                                                  #submitting login credentials

driver.quit()                                                          #Should return exit code 0 if positive test
