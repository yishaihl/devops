#Python Packages Site
#https://pypi.org/

#Example of installing package
#pip install py-mysql

from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.get("http://www.google.com")
print(driver.current_url)
print(driver.title)
print(driver.page_source)