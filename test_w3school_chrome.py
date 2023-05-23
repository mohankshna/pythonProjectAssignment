from selenium import webdriver,common
import time,pytest
from selenium.webdriver import Chrome,Firefox

@pytest.fixture
def browser():
  driver = webdriver.Chrome(executable_path=".//chromedriver.exe")
  driver.implicitly_wait(10)
  yield driver
  driver.quit()

def test_w3schools_logo(browser):

    #driver = webdriver.Chrome(executable_path=".//chromedriver.exe")
    browser.get("https://www.w3schools.com/")
    time.sleep(2)
    try:
        browser.maximize_window()
        print(browser.title)

        # ASSERT WE ARE ON THE CORRECT PAGE
        assert "w3schools" in browser.title.lower() , "W3Schools title not shown"
        assert "w3schools" in browser.page_source.lower(), "W3Schools not shown in pagesource"

        logo = browser.find_element_by_xpath("//a[@title='Home']")

        if logo.is_displayed():
            print("W3Schools logo displayed")
        else:
            raise Exception("W3Schools logo not displayed")

    finally :
        pass