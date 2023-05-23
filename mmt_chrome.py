from selenium import webdriver,common
import time

driver = webdriver.Chrome(executable_path=".//chromedriver.exe")
driver.get("http://www.makemytrip.com")
try:
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

finally :
    driver.quit()