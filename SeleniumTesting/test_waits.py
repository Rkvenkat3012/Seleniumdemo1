import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
s=Service("C:/Users/venka/PycharmProjects/SeleniumpythonProject/Drivers/chromedriver.exe")

class TestEnvatomarket():
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_waits(self,setup):
        self.driver.get("https://themeforest.net/category/site-templates/retail/travel?tags=travel%20agency&term=demo")
        waits=WebDriverWait(self.driver,10)
        element=waits.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='search-filters-checkbox_filter_component__checkbox']")))
        element.click()
        time.sleep(3)
        self.driver.close()
        print("test completed")

