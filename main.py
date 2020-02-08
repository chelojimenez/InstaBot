'''On Windows
Run shell as Administrator.

> Get-ExecutionPolicy

> Set-ExecutionPolicy remoteSigned

Done.

To Undo
> Set-ExecutionPolicy restricted
 '''

from selenium import webdriver
from time import sleep 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By


f = open("password.txt", "r")
pw = f.read()
f.close()
class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome() 

        #Go to instagram
        self.driver.get('https://www.instagram.com/accounts/login/?hl=en')
        sleep(1)
        #Log in with facebook
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/button').click()
        (sleep)
        #Send Email
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input').send_keys(username)
        #Set Password
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input').send_keys(password)
        #Get username
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        #Get password
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        
        #Login
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button').click()
        #self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)
        #NOT NOW
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
        #acpt = self.driver.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]")
        #acpt.click()
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Not Now')]"))).click()
        #self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        #self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        #ui.WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()
        sleep(4)
    def get_unfollowers(self):
        #click on username
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a/svg/path').click()
    
InstaBot("marcelojimenezrocabado@gmail.com", pw)

