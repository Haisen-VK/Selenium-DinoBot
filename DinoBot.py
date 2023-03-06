import os
from DinoEngine import DinoEngine
from dotenv import load_dotenv
"""
    Must include .env file with DRIVERPATH                  

"""
load_dotenv('.env') 
Dino = DinoEngine(os.environ.get("DRIVERPATH"),os.environ.get("OBSTACLE_DETECTION_RANGE"))
Dino.Initialize()
