from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
     driver = webdriver.Chrome()
     driver.set_window_size(1920, 1080)
     yield driver
     driver.quit()

def test_search(driver):
     driver.get('https://www.google.com/')
     driver.find_element(By.NAME, 'q').send_keys('Zulkarnen', Keys.ENTER)
     assert  'Zulkarnen' in driver.title

def test_search_habbib(driver):
     driver.get('https://www.google.com/')
     driver.find_element(By.NAME, 'q').send_keys('habib jafar', Keys.ENTER)
     assert  'habib jafar' in driver.title
     