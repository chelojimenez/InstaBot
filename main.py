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
from selenium.webdriver.common.keys import Keys

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
        self.driver = webdriver.Chrome('chromedriver.exe')
        #Go to instagram
        self.driver.get('https://www.instagram.com/accounts/login/?hl=en')
        sleep(1)
        #Get username
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        #Get password
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        #Login
        # self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        # sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(Keys.ENTER)
        #NOT NOW
        notNowButton = WebDriverWait(self.driver, 15).until(
        lambda d: d.find_element_by_xpath('//button[text()="Not Now"]'))
        notNowButton .click()
        sleep(2)
    def get_unfollowers(self):
        #click on username
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()    

my_bot = InstaBot("chelo_jimenez22", pw)
my_bot.get_unfollowers()


