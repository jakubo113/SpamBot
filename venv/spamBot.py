from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("chces spamovat cez spambota[y/n] :")
if input() == 'n' :
    print("email :")
    log = input()
    print("heslo :")
    passw = input()
else:
    log = "****"
    passw = "***"
while(True):
    print("Meno trestaneho Avatara :")
    name = input()
    if name == '****' or name == '****':
        print("Tvorcovia nesmu byt trestany svojimi vytvormi!!")
    elif name == '***':
        name = '****'
        break
    else:
        break

print("\nCim mu chces zneprijemnit zivot?: :")
spam = input()

driver = webdriver.Ie(executable_path="IEDriverServer.exe")
#driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://discord.com/login")
WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Welcome back!')]")))
driver.find_element_by_xpath('//*[@name="email"]').send_keys(log)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(passw)
driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Friends')]")))
driver.find_element_by_xpath("//*[@aria-label='Deutche Gruppen Sex :)']").click()
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'shit-post')]")))
time.sleep(1)
try:
    driver.find_element_by_xpath("//*[@aria-label='{}, Online']".format(name)).click()
except:
    try:
        driver.find_element_by_xpath("//*[@aria-label='{}, Idle']".format(name)).click()
    except:
        try:
            driver.find_element_by_xpath("//*[@aria-label='{}, Online via mobile']".format(name)).click()
        except:
            driver.find_element_by_xpath("//*[@aria-label='{}']".format(name)).click()

WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//*[@placeholder='Message @{}']".format(name))))
time.sleep(1)
driver.find_element_by_xpath("//*[@placeholder='Message @{}']".format(name)).send_keys("{}".format(spam))
driver.find_element_by_xpath("//*[@placeholder='Message @{}']".format(name)).send_keys(Keys.ENTER)
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(),'Direct Messages')]")))
while(True):
    try:
        time.sleep(0.4)
        driver.find_element_by_xpath("//*[@aria-label='Message @{}']".format(name)).send_keys("{}".format(spam))
        driver.find_element_by_xpath("//*[@aria-label='Message @{}']".format(name)).send_keys(Keys.ENTER)
    except:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Enter the chill zone')]")))
        driver.find_element_by_xpath("//*[contains(text(),'Enter the chill zone')]").click()
        time.sleep(1)

