from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("--log-level=3")
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")#filename="programa.log"

def before_all(context):
    logging.info("\033[92m Start ✔\033[0m")
    context.driver = webdriver.Chrome(options=options)

def before_scenario(context,scenario):
     logging.info(f"\033[92mWait[10s] in [{scenario}]\033[0m")
     context.driver.implicitly_wait(10)

def after_all(contex):
    logging.info("\033[92mQuit\033[0m")
    contex.driver.quit()