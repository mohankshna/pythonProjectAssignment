from selenium import webdriver,common
from selenium.webdriver.common.keys import Keys
import time,re
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(executable_path='.//geckodriver.exe',options=options)
try:
    driver.get("http://www.makemytrip.com")
    driver.maximize_window()
    print(driver.title)

    # ASSERT WE ARE ON THE CORRECT PAGE
    assert "makemytrip" in driver.title.lower() , "MakeMyTrip title not shown"
    assert "makemytrip" in driver.page_source.lower(), "MakeMyTrip not shown in pagesource"

    logo = driver.find_element_by_xpath("//*[@id='SW']//a/picture/img")

    if logo.is_displayed():
     print("MakemyTrip logo displayed")
    else:
     raise Exception("MakemyTrip logo not displayed")

finally:
    driver.close()