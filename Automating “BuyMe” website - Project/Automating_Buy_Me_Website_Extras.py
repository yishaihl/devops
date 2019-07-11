#Import Required Packages:
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
#Project variable:
driver_location = "//Users//yishaihalpert//Desktop//ChromeDriver"
website_url = "https://buyme.co.il/money/1229712"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.maximize_window()
driver.get(website_url)
driver.implicitly_wait(30)
#loading screen:
spinner_size = driver.find_element_by_id('ember572')
size = spinner_size.size
print(size)
#Home screen:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
click_item.click()
login = driver.find_elements_by_xpath('/html/body/div[1]/div/div[1]/div/div/div[3]/div/div[3]/form/button')
login[0].click()
error_message = driver.find_element_by_id('parsley-id-12').text
error_message2 = "כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה"
if error_message == error_message2:
    print("לא הוזן שם משתמש וסיסמא")
else:
    print("שם משתמש וסיסמא הוזנו בהצלחה")
#Choose gift screen:
Scroll window down:
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.save_screenshot("/Users/yishaihalpert/Desktop/screenshot.png")
#Sender & receiver information screen:
