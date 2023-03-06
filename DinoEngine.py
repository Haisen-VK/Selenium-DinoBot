from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import os

load_dotenv('.env') 

class DinoEngine:
    def __init__(self):
        #initialize Basic Things(Gets Path from .env,etc)
        self.PATH = os.environ.get("DRIVERPATH")
        self.Driver = webdriver.Chrome(self.PATH)
        self.Actions = ActionChains(self.Driver)

    def Initialize(self):
        #Code To Kickstart chrome dino game
        try:
           self.Driver.get("chrome://dino/")
        except WebDriverException:
            self.HitSpace()
            pass
        #Following Code Helps Browser to Keep Running and not Quit
        while(True):
            pass
   
    def HitSpace(self):
        #Hits Space
        self.Actions.send_keys(Keys.SPACE)
        self.Actions.perform()