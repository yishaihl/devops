#Import Required Packages:
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
#Project variable:
driver_location = "//Users//yishaihl//Desktop//ChromeDriver"
website_url = open("//Users//yishaihl//Desktop//url.txt", "r")
gift_price = "400"
sender_name = "ישי הלפרט"
receiver_name = "מאיה וויס"
blessing = "באהבה גדולה ממני!"
image_path = "/Users/yishaihl/Desktop/1.jpeg"
sender_cellphone = "0523681458"
receiver_cellphone = "0546304938"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.maximize_window()
driver.get(website_url)
driver.implicitly_wait(10)
#Press on button "״כניסה והרשמה:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "seperator-link")))
click_item.click()
#Press on button "״להרשמה:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-btn")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "text-btn")))
click_item.click()
#Enter first name:
driver.find_element_by_id("ember1037").send_keys("ישי")
#Enter e-mail address:
driver.find_element_by_id("ember1039").send_keys("yishaihl@gmail.com")
#Enter password:
driver.find_element_by_id("valPass").send_keys("Yisak888%")
#Enter password again:
driver.find_element_by_id("ember1043").send_keys("Yisak888%")
#Press radio button "אני מסכים":
driver.execute_script("arguments[0].click();",driver.find_element_by_id("ember1044-id"))
#Press button "...הרשמה":
login = driver.find_elements_by_xpath('//*[@id="ember1035"]/button')
login[0].click()
#Pick a price point:
time.sleep(4)
search_element = WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember664_chosen"]/a/span')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ember664_chosen"]/a/span')))
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
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "money")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "money")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(gift_price).perform()
search_button = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[2]/form/div[2]/div/button')
search_button[0].click()
#Press radio button "למישהו אחר":
driver.execute_script("arguments[0].click();",driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/label[1]/span[1]"))
#Enter receiver name:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/label[1]/span")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/label[1]/span")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(receiver_name).perform()
#Enter sender name:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/label[2]/span")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/label[2]/span")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(sender_name).perform()
#Enter a blessing:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[2]/textarea")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[2]/textarea")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(blessing).perform()
#Upload a picture:
time.sleep(5)
driver.find_element_by_name("fileUpload").send_keys(image_path)
#Pick the event:
time.sleep(2)
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[1]/div/a/span')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[1]/div/a/span')))
click_item.click()
#Pick "יומהולדת":
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[1]/div/div/ul/li[6]')))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[3]/label[1]/div/div/ul/li[6]')))
click_item.click()
#Press radio button "מיד אחרי התשלום":
driver.execute_script("arguments[0].click();",driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[3]/div/div[1]/label[1]"))
#Scroll window down:
element = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]")
driver.execute_script("arguments[0].scrollIntoView()", element)
#Pick Email / SMS option:
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[1]/div[1]/div/button/span/span[1]").click()
#Enter address / number and press save:
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div[1]/div/div[1]")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div[1]/div/div[1]")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(sender_cellphone).perform()
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div[1]/div/div[2]")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div[1]/div/div[2]")))
click_item.click()
actions = ActionChains(driver)
actions.move_to_element(click_item).send_keys(receiver_cellphone).perform()
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[4]/div/div[4]/div[2]").click()
#Submit:
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/div[1]/div/div/div[1]/div/div[2]/div[5]").click()




