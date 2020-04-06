"""
    Creatd by: Frédéric Peña
    on the: 30/03/2020
"""

import unittest                 #module for constructing and running tests
from selenium import webdriver  #module specific to webpages testing

class Test(unittest.TestCase):  #Creation class Test avec sousclasse unittest.TestCase
    def test_exactFind(self, UrlWebPage = "https://s1.demo.opensourcecms.com/wordpress/", IdSearched = "search-form-1" , NameSearched = "s", TextSearched = "Hello world!"):
        """This method will find several element by different attributes(Id, Name, Link Name)"""

        driver = webdriver.Firefox()    #Setting browser
        driver.get(UrlWebPage)          #Going to website tested

        """Search by ID"""
        print ('///////////////////////////////////////////////////////////////')
        print ('By ID')

        element = driver.find_element_by_id(IdSearched)
        print(element.get_attribute("placeholder"),"\n")

        """Search by name"""
        print('////////////////////////////////////////////////////////////////')
        print ('By name')

        element = driver.find_element_by_name(NameSearched)
        print(element.get_attribute("type"),"\n")

        """Search by Link Name"""
        print('////////////////////////////////////////////////////////////////')
        print('By link name')

        element = driver.find_element_by_link_text(TextSearched)
        print(element.text)

        driver.close()
        pass

    def test_missing(UrlWebPage = "https://s1.demo.opensourcecms.com/wordpress/", MissingTextSearched = "missind"):

        driver = webdriver.Firefox()    #Setting browser
        driver.get(UrlWebPage)          #Going to website tested

        """Search by Link Name"""
        print('////////////////////////////////////////////////////////////////')
        print('Missing\n')

        element = driver.find_element_by_id(MissingTextSearched)
        print(element.text)

        driver.close()
        pass



