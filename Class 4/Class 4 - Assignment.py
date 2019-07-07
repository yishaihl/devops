#1.a-b
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
#1st tab
driver.get('http:/www.walla.co.il')
#second tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('http://www.ynet.co.il')

#2.a-c
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
#1st tab
driver.get('http:/www.walla.co.il')
#second tab
driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get('http://www.ynet.co.il')
tab2_title = driver.title
driver.refresh()
print(tab2_title)
if driver.title == tab2_title:
    print("Match")
else:
    print("Not Match")

#3
#Yes they are the same because the code is the same, the browser is only the interpreter.

#4.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.get('https://translate.google.com/')
driver.find_element_by_id("source").send_keys(u'בדיקה')

#5.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.implicitly_wait(10)
driver.get('https://www.youtube.com/')
driver.find_element_by_id("search").send_keys("Pink Floyd High Hopes")
driver.find_element_by_id("search-icon-legacy").click()

#6.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.get('https://translate.google.com/')
by_id = driver.find_elements_by_id("source")
by_class = driver.find_elements_by_class_name("orig tlid-source-text-input goog-textarea")
by_link_text = driver.find_elements_by_link_text("spellcheck")
print(str(by_id) + "\n" + str(by_class) + "\n" + str(by_link_text))

#7.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
driver.find_element_by_id("email").send_keys("yishaihl@gmail.com")
driver.find_element_by_id("pass").send_keys("")
driver.find_element_by_id("u_0_2").click()

#8.Challenges

#8.
from selenium import webdriver
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
driver.delete_all_cookies()
get_cookies = driver.get_cookies()
print(get_cookies)

#9.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.implicitly_wait(3)
driver.get('https://github.com/')
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]").send_keys("Selenium")
search_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/div/ul[3]/li[2]/a/div[2]")))
ActionChains(driver).move_to_element(search_element).perform()
click_item = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/div/ul[3]/li[2]/a/div[2]")))
click_item.click()

#10.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
driver = webdriver.Chrome(executable_path="//Users//yishaihalpert//Desktop//ChromeDriver")
driver.get('https://translate.google.com/')
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")