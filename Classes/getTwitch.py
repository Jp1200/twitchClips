import numpy as np
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Clips:
    def __init__(self):
        self.data = []
        self.driver = webdriver.Chrome()

    def getClips(self, query):

        if (type(query) != str):
            print("Query not of type string.")
        else:
            d = self.driver
            d.get(query)
            assert "Python" in d.title
            elem.d.find_element_by_name("q")
            print(elem)
            elem.clear()
            elem.send_keys("pycon")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in d.page_source
            d.close()


q = "http://www.python.org"
result = Clips.getClips(q)

print(q)
