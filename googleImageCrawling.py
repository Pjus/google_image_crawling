from selenium import webdriver
import time
import os
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains 

driver = webdriver.Chrome('./chromedriver') #, chrome_options=chrome_options
driver.implicitly_wait(3)

url = f"https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.co.kr%2F&ec=GAZAAQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
driver.get(url)

mail_address = input('e-mail')
password = input("password")

driver.find_element_by_id("identifierId").send_keys(mail_address)
driver.find_element_by_id("identifierNext").click()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_id("passwordNext").click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="gbw"]/div/div/div[1]/div[2]/a').click()
query = input('query')
# query = 'cat'

driver.find_element_by_class_name("gLFyf.gsfi").send_keys(query)
driver.find_element_by_class_name("gLFyf.gsfi").send_keys(Keys.RETURN)

# driver.find_element_by_xpath('//*[@id="islmp"]/div/div[1]/div/a[2]').click()

if not os.path.exists('./downloads/' + str(query)):
    os.makedirs('./downloads/' + str(query))

path = './downloads/' + str(query) + '/'

time.sleep(1)

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
more = '//*[@id="islmp"]/div/div/div/div/div[5]/input'
n = 1

while True:
    # Scroll down to bottom                                                      
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)                                               
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height          
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            driver.find_element_by_xpath(more).click()
        except:
            break

    last_height = new_height
    print(last_height)

all_pic = driver.find_elements_by_class_name('rg_i.Q4LuWd')
print(len(all_pic))
pic_link = []
for pic in all_pic:
    try:
        pic.click()
        time.sleep(2)
        src = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute('src')
        # print(src)
        # download the image
        if src == None:
            pass
        else:
            pic_link.append(src)
            urllib.request.urlretrieve(src, path + "{}.png".format(n)) #
            print(n)
            n += 1
    except:
        continue