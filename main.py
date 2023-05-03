import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

att = Service(ChromeDriverManager().install())

fire = webdriver.Chrome(service=att)
fire.get("https://dashboard.cloudpark.com.br/login/")



#dados basicos
email = ""
senha = ""

#fire era de firefox

#login
fire.find_element('xpath','//*[@id="mat-input-0"]').send_keys(email) #email
fire.find_element('xpath','//*[@id="mat-input-1"]').send_keys(senha) #senha
fire.find_element('xpath','//*[@id="content-wrapper"]/section/login/div/form/div[4]/button').click() #faz login

#aguarda 10 segundos para carregar a pagina
time.sleep(10)

#muda patio 
fire.find_element('xpath', '/html/body/app-root/mat-drawer-container/mat-drawer/div/main-menu/section/ul/li[2]/mat-form-field/div/div[1]/div').click() #seleciona o menu de patios
fire.find_element('xpath','/html/body/div[3]/div[2]/div/div/div/mat-option[3]/span').click() #seleciona cib

#entra em clientes/plano para criar um plano
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer/div/main-menu/section/mat-tree/mat-nested-tree-node[2]/ul[1]/li/div/span/span').click() # clica em Clientes
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer/div/main-menu/section/mat-tree/mat-nested-tree-node[2]/ul[2]/mat-nested-tree-node[2]/li/div').click() # seleciona planos 

#criando plano
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer-content/div/section/customer-plan-list/div[1]/mat-toolbar/button').click() # adicionar plano
fire.find_element('xpath','//*[@id="mat-input-4"]').send_keys('Rodrigo') #Nome
fire.find_element('xpath','//*[@id="mat-radio-4"]').click() #tipo de plano
fire.find_element('xpath','//*[@id="mat-input-5"]').send_keys('1000') #valor
fire.find_element('xpath','//*[@id="mat-checkbox-2"]/label').click() #controle de vagas
fire.find_element('xpath','//*[@id="mat-input-8"]').send_keys('5') #total de veiculos
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer-content/div/section/customer-plan-item/div[1]/form/div[2]/button').click() #salvar

#cria cliente e adiciona o plano
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer/div/main-menu/section/mat-tree/mat-nested-tree-node[2]/ul[2]/mat-nested-tree-node[1]/li/div').click()#  clientes/clientes
fire.find_element('xpath','//*[@id="body"]/app-root/mat-drawer-container/mat-drawer-content/div/section/customer-list/div[2]/mat-toolbar/button[1]').click() #adicionar cliente
fire.find_element('xpath','//*[@id="mat-input-10"]').send_keys("Rodrigo") #nome
fire.find_element('xpath','//*[@id="mat-tab-label-0-2"]').click() #Plano
fire.find_element('xpath','//*[@id="mat-select-value-11"]').click() #menu planos 
button = fire.find_element(By.XPATH,"//span[contains(@class,'mat-option-text')][contains(text(),'Rodrigo - R$ 10,00')]").click()
time.sleep(2)
fire.find_element('xpath','/html/body/app-root/mat-drawer-container/mat-drawer-content/div/section/customer-item/div[1]/form/div/button').click() #salvar
time.sleep(2)
fire.find_element('xpath','/html/body/div[3]/div[2]/div/mat-dialog-container/confirm-transaction-dialog/div[2]/button[2]').click() #salvar salvar
