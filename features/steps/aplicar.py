from behave import given,when,then
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")#filename="programa.log"


@given(u'conectar ao dontPad')
def step_impl(context):
    url='https://dontpad.com/'
    try:
     context.driver.get(url)
     context.driver.implicitly_wait(10)
     time.sleep(2)
     logging.info("\033[92mconexao com {url} [✔]\033[0m")
    except:
     logging.error("\033[31mErro na conexao com : {url}\033[0m"+url)
     context.driver.quit()
     context.quit()


@when(u'gerar uma lista de nomes aleatorios')
def step_impl(context):
    fake = Faker()
    nomes = [fake.name() for _ in range(10)]
    with open('./nomes.txt', 'w') as arquivo:
        for nome in nomes:
            arquivo.write(nome + '\n')
    
@when(u'incluir nome ao search')
def step_impl(context):
    campo_busca = context.driver.find_element(By.ID, "search")
    campo_busca.click()
    with open("nomes.txt") as file:
        nomes = file.readlines()
    nome = random.choice(nomes).strip()
    campo_busca.send_keys(nome)
@when(u'clicar em ok')
def step_impl(context):
    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/section/form/button')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)

@when(u'escrever o link de negocios')
def step_impl(context):
    campo_busca = context.driver.find_element(By.ID, "text")
    campo_busca.click()
    with open("negocios.txt") as file:
        link = file.readlines()
    campo_busca.send_keys(link)
@when(u'voltar')
def step_impl(context):
    time.sleep(3)
    context.driver.back()

@when(u'incluir nome ao search novamente')
def step_impl(context):
    time.sleep(10)
    campo_busca = context.driver.find_element(By.ID, "search")
    campo_busca.clear()
    campo_busca.click()
    with open("nomes.txt") as file:
        nomes = file.readlines()
    nome = random.choice(nomes).strip()
    campo_busca.send_keys(nome)
    
@when(u'clicar em ok novamente')
def step_impl(context):

    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/section/form/button')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)

@then(u'escrever o link de tecnologia')
def step_impl(context):
    campo_busca = context.driver.find_element(By.ID, "text")
    campo_busca.click()
    with open("tecnologia.txt") as file:
        link = file.readlines()
    campo_busca.send_keys(link)
    time.sleep(5)