from behave import given,when,then
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")#filename="programa.log"


@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    url='https://ge.globo.com/'
    try:
     context.driver.get(url)
     context.driver.implicitly_wait(10)
     time.sleep(2)
     logging.info("\033[92mconexao com {url} [✔]\033[0m")
    except:
     logging.error("\033[31mErro na conexao com : {url}\033[0m"+url)
     context.driver.quit()
     context.quit()


@when(u'clico no menu NBA')
def step_impl(context):
  action = ActionChains(context.driver) 
  menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[1]/header/div[2]/div/div/div[1]/div')))
  action.move_to_element(menu).click().perform()
  time.sleep(3)
  menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/nav/div/div[1]/ul/li[12]/a/span[1]')))
  action.move_to_element(menu).click().perform()
  time.sleep(3)
  menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/nav/div/div[1]/ul/li[12]/ul/li[3]/a/span[1]')))
  action.move_to_element(menu).click().perform()
  time.sleep(10)
    
@when(u'classificacao for exibida')
def step_impl(context):
    print("to com preguiça")



@then(u'devo saber quem sao os primeiros colocados')
def step_impl(context):
    print("to com preguiça")