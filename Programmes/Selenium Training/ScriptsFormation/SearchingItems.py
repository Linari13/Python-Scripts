"""
************************************
* Searching Elements within a page *
************************************
"""

import unittest
from selenium import webdriver

class Test(unittest.TestCase):

    def test_searching(UrlWebPage = "https://s1.demo.opensourcecms.com/wordpress/"):
        driver = webdriver.Firefox()    # Setting browser
        driver.get(UrlWebPage)          # Going to website tested

        print ('///////////////////////////////////////////////////////////////')
        print ('By ID')

        elements = driver.find_elements_by_partial_link_text("link")
        for element in elements:
            print(element.text)

        print ('\n///////////////////////////////////////////////////////////////')
        print ('By Tag Name')

        elements = driver.find_elements_by_tag_name("li")
        for element in elements:
            print(element.text)

        print ('\n///////////////////////////////////////////////////////////////')
        print ('By Class Name')

        elements = driver.find_elements_by_class_name("widget-title")
        for element in elements:
            print(element.text)

        print ('\n///////////////////////////////////////////////////////////////')
        print ('By CSS Selector')

        print("\n Specific")
        elements = driver.find_elements_by_css_selector(".imprint")
        for element in elements:
            print(element.text)

        print("\n Generic CSS")
        elements = driver.find_elements_by_css_selector("section > h2")
        for element in elements:
            print(element.text)

        print ('\n///////////////////////////////////////////////////////////////')
        print ('By xpath')

        print("\n specific xpath")
        elements = driver.find_elements_by_xpath("//li[@class='recentcomments']")
        for element in elements:
            print(element.text)

        print("\n Generic")
        elements = driver.find_elements_by_xpath("//body//li")
        for element in elements:
            print(element.text)

        print('\n////////////////////////////////////////////////////////////////')
        print('Missing\n')

        """Test quand aucun resultat"""
        elements = driver.find_elements_by_class_name("madeup")
        for element in elements:
            print(element.text)

        driver.close()
        pass


if __name__ == "main":
    if __name__ == '__main__':
        #import sys;sys.argv = ["", "Test.testName" ]
        unittest.main()

    test_searching()