#!/usr/bin/env python3
# coding: utf-8

import time, os, sys, logging
from sendmail import *
from datetime import datetime
from pathlib import Path
from shutil import move
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.core.logger import set_logger
from webdriver_manager.microsoft import EdgeChromiumDriverManager

###### DEBUG MODE #####
debug = "ON"
#debug = "OFF"

###### Variaveis pertinentes #####
#driverPath = "/usr/local/bin/chromedriver"
driverService=Service(EdgeChromiumDriverManager().install())
scriptPath = "/opt/selenium/"
homeDir = "/home/leitao/"
date_time_obj = datetime.now().strftime("%Y%m%d""-""%H-%M")
screenShot = scriptPath+"/ScreenShot/EV/ev-"+date_time_obj+".png"
htmlOpen = scriptPath+"/HTML//my_mon.html"
logOpen = scriptPath+"/logs//Log_my_mon.txt"


if debug == "ON":
    print("Abrindo navegador com interface")
    options = Options()
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Edge(service=driverService,options=options)
else:
    print("Abrindo navegador sem interface")
    options = Options()
    #options.headless = True
    options.add_argument("--headless")
    options.add_argument('window-size=1920x1080')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Edge(service=driverService,options=options)

driver.get("https://www.python.org")
time.sleep(6)
print(driver.title)
#time.sleep(2)
search_bar = driver.find_element(By.NAME, "q")
#search_bar = driver.find_element("name", "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)
search_bar.submit()
print(driver.current_url)
time.sleep(12)
driver.close()