
import random 
import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller

class linkedinBot:
    
    #input through csv
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")  #declaring the driver basically we are telling it to open chrome broswer
       

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver #making instance
        driver.get("https://www.linkedin.com/login?") #calling linkedin
        
        #finding login button with xpath
        login_button = driver.find_element_by_xpath('//*[@type="submit"]')
        login_button.click()

        time.sleep(20)

        #finding usernameBox button with xpath
        username_elem = driver.find_element_by_xpath('//*[@id="username"]')
        username_elem.clear()
        username_elem.send_keys(self.username)

        time.sleep(20)

        #finding passwordBox button with xpath
        passworword_elem = driver.find_element_by_xpath('//*[@id="password"]')
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        
        #
        passworword_elem.send_keys(Keys.RETURN)
    
    def logout(self):
        driver = self.driver
        dropdownButton = driver.find_element_by_css_selector('#nav-settings__dropdown-trigger')
        dropdownButton.click()
        
        time.sleep(20)

        signoutButton = driver.find_element_by_xpath('//*[@href="/m/logout/"]')
        signoutButton.click()



    def like_photo(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/posts/rudresh-kapoor-bbbbb88b_thailands-wealthiest-man-dhanin-chearavanont-activity-6612381063052386304-Ur9j/")
        
        self.like_button = driver.find_element_by_class_name("react-button__trigger")
        self.like_button.click()
        
    def like_photo1(self,pl):
        driver = self.driver
        driver.implicitly_wait(20000)
        time.sleep(2)
        driver.get(pl) #taking postLink as input
        
        self.like_button = driver.find_element_by_class_name("react-button__trigger")
        self.like_button.click()
        
    def movement(self):   #function for movements of mouse so that its cant detect its a bot
        mouse = Controller()
        mouse.position = (10, 20)
        mouse.move(60, -150)
        mouse.move(20, -17)
        mouse.move(30, -40)
        mouse.scroll(0, 2)
        mouse.scroll(0, -100)    
        mouse.scroll(0,-120)    

driver = webdriver.Chrome("./chromedriver")

df = pd.read_csv("uid.csv",usecols=['username','password'])

l=[]

i,j=10,0

while i>0: #j=len(df)
    # x=2
    # while(x>0):
    #     rand=random.randint(0,2)
    #     if rand in l:
    #        continue
    #     else:
    #         l.append(rand)
    #         j=rand
    #     x-=1     
    
    us=df.username[j]
    ps=df.password[j]
    j+=1
    raji1= linkedinBot(us,ps)
    raji1.login()
    time.sleep(20)
    raji1.like_photo()
    time.sleep(10)
    raji1.movement()
    raji1.logout()
    time.sleep(60)
    raji1.closeBrowser()
  #  driver = raji1.driver
    driver.get("https://www.google.com/")
    #time.sleep(10)
    bro="chrome.exe"
    os.system("taskkill /f /im "+ bro)
        
    #driver.implicitly_wait(600000)
    
    i-=1
    
i,j=7,0
while i>0:
    us=df.username[j]
    ps=df.password[j]
    j+=1
    raji1= linkedinBot(us,ps)
    raji1.login()
    df1= pd.read_csv("post.csv")
    for k in range(len(df1)):
        raji1.like_photo1(df1.PostLink[k])


    i-=1
    raji1.logout()
    time.sleep(60)
    #driver.implicitly_wait(600000)
    time.sleep(60)
