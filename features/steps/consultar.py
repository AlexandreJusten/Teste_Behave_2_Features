from behave import given,when,then
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")#filename="programa.log"


@given(u'acesso a pagina inicial do google news')
def step_impl(context):
    url='https://news.google.com/home?hl=pt-BR&gl=BR&ceid=BR:pt-419'
    try:
     context.driver.get(url)
     context.driver.implicitly_wait(10)
     time.sleep(2)
     logging.info("\033[92mconexao com {url} [✔]\033[0m")
    except:
     logging.error("\033[31mErro na conexao com : {url}\033[0m"+url)
     context.driver.quit()
     context.quit()


@when(u'clico no menu ciencia e tecnologia')
def step_impl(context):
  action = ActionChains(context.driver) 
  menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/header/div[3]/div/c-wiz/div[1]/div[10]/a')))
  action.move_to_element(menu).click().perform()
  time.sleep(3)
    
@when(u'os dados forem exibidos')
def step_impl(context):
    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/c-wiz[2]/div/main/c-wiz/div[1]/div[2]/span/span/button')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)

@when(u'devo clicar em compartilhar e copiar o link')
def step_impl(context):

    share_button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Copiar link"]')))
    share_button.click()
    
    import pyperclip
    link = pyperclip.paste()
    with open('./tecnologia.txt', 'w') as arquivo:
      arquivo.write(link)
    assert link != '', "Link não foi copiado para a área de transferência"

@when(u'devo clicar em fechar')
def step_impl(context):
    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[13]/div[2]/div/button')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)
  
@when(u'devo clicar em negocios')
def step_impl(context):
    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/header/div[3]/div/c-wiz/div[1]/div[9]/a')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)

@when(u'devo clicar em compartilhar novamente')
def step_impl(context):
    action = ActionChains(context.driver) 
    menu = WebDriverWait(context.driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/c-wiz[3]/div/main/c-wiz/div[1]/div[2]/span/span/button')))
    action.move_to_element(menu).click().perform()
    time.sleep(3)

@then(u'copiar o link')
def step_impl(context):
    share_button = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Copiar link"]')))
    share_button.click()
    
    import pyperclip
    link = pyperclip.paste()
    with open('./negocios.txt', 'w') as arquivo:
      arquivo.write(link)
    assert link != '', "Link não foi copiado para a área de transferência"
