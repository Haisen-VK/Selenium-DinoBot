import os
from DinoEngine import DinoEngine
from dotenv import load_dotenv
"""
    Must include .env with DRIVERPATH                  

"""
load_dotenv('.env') 
Dino = DinoEngine(os.environ.get("DRIVERPATH"))
Dino.Initialize()
