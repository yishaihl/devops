
#Import Required Packages:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Chrome exacutable path variable:
driver_location = "//Users//yishaihalpert//Desktop//ChromeDriver"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.implicitly_wait(3)
driver.get("https://buyme.co.il/")
#Press on button "״כניסה והרשמה:
driver.implicitly_wait(10)
driver.find_elements_by_id("ember591")

#//*[@id="ember591"]/div/ul[1]/li[3]
#//*[@id="ember591"]/div/ul[1]/li[3]/a/span[1]