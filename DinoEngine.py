from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException


class DinoEngine:
    def __init__(self,PATH,OBSTACLE_DETECTION_RANGE):
        #initialize Basic Things(Gets Path from .env,etc)
        self.PATH = PATH
        self.OBSTACLE_DETECTION_RANGE = int(OBSTACLE_DETECTION_RANGE)
        self.Driver = webdriver.Chrome(self.PATH)
        self.Actions = ActionChains(self.Driver)
        self.tRex = object
        self.nxtObstacles  = object
        self.PastObstacles = []
        
    def Initialize(self):
        #Code To Kickstart chrome dino game
        try:
           self.Driver.get("chrome://dino/")
        except WebDriverException:
             pass
        self.HitKey(Keys.SPACE)
        self.ScanObstacles()
        while(True):
            pass
        

    def HitKey(self,Key):
        #Hits Space
       
            self.Actions.key_down(Key).pause(0.1).key_up(Key).perform()


    def ScanObstacles(self):
        
        while(True):
          
            self.tRex = self.Driver.execute_script("return Runner.instance_.tRex")
            self.nxtObstacles  = self.Driver.execute_script("return Runner.instance_.horizon.obstacles.find(o => o.xPos > Runner.instance_.tRex.xPos);")
            if(self.nxtObstacles!=[] and self.nxtObstacles!=self.PastObstacles):
                self.PastObstacles=self.nxtObstacles
                self.Driver.execute_script("console.log(Runner.instance_.horizon.obstacles)")
                self.SelectState()
    def SelectState(self):
                   

        	if(self.nxtObstacles and ( self.nxtObstacles['xPos'] - self.tRex['xPos'] ) <=  self.OBSTACLE_DETECTION_RANGE):
                    if(self.nxtObstacles["typeConfig"]["type"] == "CACTUS_LARGE" or self.nxtObstacles["typeConfig"]["type"] == "CACTUS_SMALL" or (self.nxtObstacles["typeConfig"]["type"] == "PTERODACTYL" and self.nxtObstacles['yPos']>=75)):
                        self.HitKey(Keys.SPACE)
                    if(self.nxtObstacles["typeConfig"]["type"] == "PTERODACTYL" and self.nxtObstacles['yPos']<75):
                        self.HitKey(Keys.ARROW_DOWN)
                        
                     
                        
	