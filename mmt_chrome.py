from selenium import webdriver,common
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=".//chromedriver.exe")
driver.get("http://www.makemytrip.com")
act = ActionChains(driver)
try:
    driver.maximize_window()
    act_title=driver.title
    print(act_title)
    driver.implicitly_wait(10)

    # ASSERT WE ARE ON THE CORRECT PAGE
    assert "makemytrip" in driver.title.lower() , "MakeMyTrip title not shown"
    assert "makemytrip" in driver.page_source.lower(), "MakeMyTrip not shown in pagesource"

    logo = driver.find_element_by_xpath("//*[@id='SW']//a/picture/img")

    if logo.is_displayed():
        print("MakemyTrip logo displayed")
    else:
        raise Exception("MakemyTrip logo not displayed")

    source = 'Pune'
    destination = 'Bangalore'

    #Selecting Oneway from Hyd to Tirupathi on Apr 25 2023
    ONE_WAY=driver.find_element_by_xpath("//li[@data-cy='oneWayTrip']")
    time.sleep(2)
    if ONE_WAY.is_enabled():
     source = driver.find_element_by_xpath("//input[@id='fromCity']").send_keys(source)
     time.sleep(2)
     act.send_keys(Keys.DOWN, Keys.ENTER).perform()
     time.sleep(2)
     destination=driver.find_element_by_xpath("//input[@id='toCity']").send_keys(destination)
     time.sleep(2)
     act.send_keys(Keys.DOWN, Keys.ENTER).perform()
     time.sleep(2)
     date=driver.find_element_by_xpath("//div[@aria-selected='true']//p[2]").click()
     time.sleep(2)

     search=driver.find_element_by_xpath("//a[contains(text(),'Search')]").click()
     time.sleep(2)
     title=driver.title

     if len(title) < len(act_title):
         print("Different Flights page displayed")
     else:
         raise Exception("Different Flights page not displayed")
     page=driver.page_source
     if "Flights from" in page:
         print("Search Flights page displayed")
     else:
         raise Exception("Search Flights page not displayed")
     # flicode=driver.find_element_by_xpath("//p[class='fliCode']")
     # print(flicode)



finally :
    driver.quit()
    pass