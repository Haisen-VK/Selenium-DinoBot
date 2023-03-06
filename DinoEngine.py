from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

class DinoEngine:
    def __init__(self,PATH):
        #initialize Basic Things(Gets Path from .env,etc)
        self.PATH = PATH
        self.Driver = webdriver.Chrome(self.PATH)
        self.Actions = ActionChains(self.Driver)
        self.nxtObstacles = None
        self.tRex = None
        self.PastObstacles = []
        
    def Initialize(self):
        try:
           self.Driver.get("chrome://dino/")
        except WebDriverException:
             pass
        
        #⬆️ Code To Kickstart chrome dino game
        self.Driver.execute_script("console.log('Looking for Obstacles....')")
        
        self.HitKey(Keys.SPACE)
        self.ScanObstacles()
        while(True):
            pass
        

    def HitKey(self,Key):
        #Hits Key
       
            self.Actions.key_down(Key).pause(0.1).key_up(Key).perform()


    def ScanObstacles(self):
        
        while(True):
            self.tRex = self.Driver.execute_script("return Runner.instance_.tRex")
            self.nxtObstacles  = self.Driver.execute_script("return Runner.instance_.horizon.obstacles.find(o => o.xPos > Runner.instance_.tRex.xPos);") #Function to determine Consecutive Obstacle
            
            if(self.nxtObstacles!=[] and self.nxtObstacles!=self.PastObstacles): #This IF is Improvised For Debugging
                self.PastObstacles=self.nxtObstacles
                self.Driver.execute_script("console.log(Runner.instance_.horizon.obstacles)")
                self.SelectState()
    
    def SelectState(self): #Obstacle Detection & Player Movement
                   
        	if(self.nxtObstacles and ( self.nxtObstacles['xPos'] - self.tRex['xPos'] ) <=  120):
                    if(self.nxtObstacles["typeConfig"]["type"] == "CACTUS_LARGE" or self.nxtObstacles["typeConfig"]["type"] == "CACTUS_SMALL" or (self.nxtObstacles["typeConfig"]["type"] == "PTERODACTYL" and self.nxtObstacles['yPos']>=75) ): # ⬅️ Checks if PETRODACTYL is at a Lower Position (Yaxis is inverted)                  
                        self.HitKey(Keys.SPACE)
                    if(self.nxtObstacles["typeConfig"]["type"] == "PTERODACTYL" and self.nxtObstacles['yPos']<75):  # ⬅️ Checks if PETRODACTYL is at a Higher Position (Yaxis is inverted)
                        self.HitKey(Keys.ARROW_DOWN)
                        
                     
                        
	