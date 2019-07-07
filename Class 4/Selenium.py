from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.get("https://translate.google.com/")
print(driver.current_url)
print(driver.title)
#print(driver.page_source)
#driver.quit closes all the current session allocation - cookies, proccesses etc..
#driver.close();
#driver.quit();
#driver.back/forward/refresh - perform simple webpage tasks.
#driver.back()

#Those are used locators in webpage: ID,Name,LinkedTexr,Partial LinkedText,Class Name,Xpath.
#Example:
#driver.find_element(By.ID,value="source")
#driver.find_element_by_name("q")
#Use elements for the whole 'elements' of the webpage.
#driver.find_elements_by_name("tag")
#Find link text:
#driver.find_elements_by_link_text("Click Now") #For link Text
#driver.find_elements_by_partial_link_text("Click") # For Partial Link Text.
#my_list = driver.find_elements_by_id("source")
#print(len(my_list))

#Xpath - find more focused element when you don't have ID,Name using web page hierarchy absolute / relative path:
#We can use Xpath helper plugin which gives the absolute path of an object inside the code.
#driver.find_elements_by_xpath()
#driver.findElement(By.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div")).sendKeys("Yishai Halpert");

#Send Keys
#source = driver.find_element_by_id("source").send_keys("hello")
#source = driver.find_element_by_id("source").clear()

#Verification & Assert - find attributes inside elements.
#source_element = driver.find_element_by_id("source")
#if source_element.is_enabled():
#    source_element.click()
#print(source_element.get_attribute("autocomplete"))

#Wait for the element's to be ready before executing the code.
#driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
#driver.implicitly_wait(10)
#source_element = driver.find_element_by_id("source")

#Using keyboard keys - TAB,Escape,Delete,F5.
from selenium.webdriver.common.keys import Keys
driver.find_element_by_id("source").send_keys("hello")
driver.find_element_by_id("source").send_keys(Keys.ENTER)
# use ctrl+shift+c to choose drop down elements when i'm using inspect.
# use 'submit' to submit forms / next pages.