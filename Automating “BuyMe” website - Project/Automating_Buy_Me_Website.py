#Import Required Packages:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
#Project variable:
driver_location = "//Users//yishaihl//Desktop//ChromeDriver"
website_url = "https://buyme.co.il/"
giftcard_price = "400"
receiver_name = "מאיה וויס"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.maximize_window()
driver.get(website_url)
driver.implicitly_wait(30)
#Press on button "״כניסה והרשמה:
#search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
#ActionChains(driver).move_to_element(search_element).perform()
#click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
#click_item.click()
#Press on button "״להרשמה:
#search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-btn")))
#ActionChains(driver).move_to_element(search_element).perform()
#click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-btn")))
#click_item.click()
#Enter first name:
#driver.find_element_by_id("ember1037").send_keys("ישי")
#Enter e-mail address:
#driver.find_element_by_id("ember1039").send_keys("yishaihl@gmail.com")
#Enter password:
#driver.find_element_by_id("valPass").send_keys("Yisak888%")
#Enter password again:
#driver.find_element_by_id("ember1043").send_keys("Yisak888%")
#Press radio button "אני מסכים":
#driver.execute_script("arguments[0].click();",driver.find_element_by_id("ember1044-id"))
#Press button "...הרשמה":
#login = driver.find_elements_by_xpath('//*[@id="ember1035"]/button')
#login[0].click()
#Pick a price point:
search_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember664_chosen"]/a/span')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember664_chosen"]/a/span')))
click_item.click()
#Pick ש״ח 300-499:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[1]/div/ul/li[5]')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[1]/div/ul/li[5]')))
click_item.click()
#Pick the area:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember679_chosen"]')))
ActionChains(driver).move_to_element(search_element).perform()                                                                       
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember679_chosen"]')))
click_item.click()                                                                                                                   
#Pick ת״א והסביבה:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[2]/div/ul/li[2]')))
ActionChains(driver).move_to_element(search_element).perform()                                                                                 
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[2]/div/ul/li[2]')))
click_item.click()
#Pick category:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember689_chosen"]')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember689_chosen"]')))
click_item.click()
#Pick גיפט קארד למסעדות שף:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[3]/div/ul/li[3]')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/header/div[4]/div/form/div[3]/div/ul/li[3]')))
click_item.click()
#Press the search button:
search_button = driver.find_elements_by_xpath('//*[@id="ember724"]')
search_button[0].click()
#Pick a business:
pick_business = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/a[2]/div')
pick_business[0].click()
#Type a price:
search_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "money")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "money")))
enter_number = click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(giftcard_price).perform()
search_button = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/form/div[2]/div/button')
search_button[0].click()
#Press radio button "למישהו אחר":
driver.execute_script("arguments[0].click();",driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/label[1]/span[1]"))
#Enter receiver name:
driver.execute_script("arguments[0].click();",driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/label[1]/span"))





