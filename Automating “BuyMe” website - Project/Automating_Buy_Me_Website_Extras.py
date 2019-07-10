#Import Required Packages:
from selenium import webdriver
#Project variable:
driver_location = "//Users//yishaihl//Desktop//ChromeDriver"
website_url = "https://buyme.co.il/"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.maximize_window()
driver.get(website_url)
#loading screen:
spinner_size = driver.find_element_by_id('ember572')
size = spinner_size.size
print(size)


