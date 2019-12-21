
from selenium import webdriver
#import pandas as pd
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome()
class linkedinBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/login?")
        login_button = driver.find_element_by_xpath('//*[@type="submit"]')
        login_button.click()
       # time.sleep(2)
        username_elem = driver.find_element_by_xpath('//*[@id="username"]')
        username_elem.clear()
        username_elem.send_keys(self.username)

        passworword_elem = driver.find_element_by_xpath('//*[@id="password"]')
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
#//*[@id="ember105"]/span/span

       # driver.switch_to_window('https://dms.licdn.com/playlist/C5605AQHA1-eNv1bxgQ/feedshare-captions-thumbnails-dualWrite-inhouse-mp4_h264_aac_1600k/0?e=1576922400&v=beta&t=1Jyh6ZqGr4ZTebHpmwZ8MwLn4eSWWp8CdN3NpQcCSl4')

    def like_photo(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/posts/trell-employee1-82a17319a_ohayo-activity-6613784927496441856-PFml")
            
            
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # try:
        
        #     driver.find_element_by_partial_link_text("Like Trell Employee1's post").click()
    
               
        # except Exception :
        #     pass


        driver.get("https://www.linkedin.com/posts/trell-employee1-82a17319a_hello-world-activity-6613761565021827072-bok1")
        like_button = driver.find_element_by_partial_link_text("Like Trell Employee1's post").click()
        like_button.click()
        #self.closeBrowser()

rajiIG0 = linkedinBot("trellemployee1@gmail.com","muj#1234")
rajiIG0.login()
rajiIG0.like_photo()
#//*[@id="ember105"]/span/span

rajiIG1= linkedinBot("trellemployee2@gmail.com","muj#1234")
rajiIG1.login()
rajiIG1.like_photo()
# rajiIG1.closeBrowser()
# rajiIG2= linkedinBot("trellemployee3@gmail.com","muj#1234")
# rajiIG2.login()
# rajiIG2.like_photo()
# rajiIG2.closeBrowser()

