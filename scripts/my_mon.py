#!/usr/bin/env python3
# coding: utf-8

# In[12]:


import time, os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from pathlib import Path
from shutil import move
from sendmail import *

# In[13]:

### DEBUG ### ON or OFF
debug = "ON"
#debug = "OFF"

#Variaveis Globais
rootPath = "/opt/selenium/"
driverPath = '/usr/local/bin/chromedriver'
homeDir = "/home/leitao/"

########
date_time_obj = datetime.now().strftime("%Y%m%d""-""%H-%M")
screenShot = rootPath+"/ScreenShot/EV/ev-"+date_time_obj+".png"
htmlOpen = rootPath+"/HTML//ev.html"
logOpen = rootPath+"/logs//LogEv.txt"

# In[15]:


if debug == "ON":
    print("Abrindo navegador com interface")
    options = Options()
    options.add_argument('window-size=1920x1080')
    navegador = webdriver.Chrome(executable_path=driverPath,options=options)
else:
    print("Abrindo navegador sem interface")
    #options = Options()
    #options.add_argument("--headless")
    #options.add_argument('window-size=1920x1080')
    options = Options()
    options.headless = True
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
    navegador = webdriver.Chrome(executable_path=driverPath,options=options)


# In[16]:


def gravaLogFail():
    f = open(logOpen, 'a')
    f.write("Consulta não realizada " +date_time_obj + "\n") 
    f.close()
    w = open(htmlOpen, 'w')
    w.write("Consulta não Realizada" +date_time_obj  + "\n")
    print ('Saindo..')
    navegador.save_screenshot(screenShot)
    time.sleep(2)
def gravaLogPass():
    with open(logOpen, "r") as file:
        for last_line in file:
            pass
        if 'não' in last_line:
            mailSend('[Enquadramento] Voltou a recarregar a página', 'Enquadramento voltou a normalidade')
    f = open(logOpen, 'a')
    f.write("Consulta realizada " +date_time_obj + "\n")
    f.close()
    w = open(htmlOpen, 'w')
    w.write("Consulta realizada com Sucesso - " +date_time_obj + "\n")
    w.close()
    print ('Saindo..')
    time.sleep(2)


# In[17]:


def carregaPagina():
    try:
        print("Carregando página...")
        time.sleep(2)
        navegador.get('https://enquadramentoveiculo.cnseg.org.br')
        time.sleep(30)
        navegador.find_element_by_id('inputPassword')
        print ("Carregada!")
        return
    except NoSuchElementException:
        try:
            print ("Entrou no Except, tentando novamente")
            time.sleep(15)
            navegador.get('https://enquadramentoveiculo.cnseg.org.br')
            time.sleep(3330)
            navegador.find_element_by_id('inputPassword')
            print ("Carregou a página")
        except NoSuchElementException:
            try:
                print ("Entrou no Except, pagina nao carregada")
                navegador.save_screenshot(screenShot)
                mailSend('[Enquadramento] Nao foi possível abrir a pagina', 'Enquadramento nao abriu a pagina')
                time.sleep(5)
                gravaLogFail()
                navegador.quit()
                sys.exit()
            except:
                navegador.quit()
                sys.exit()


# In[18]:


#Login
def preencheLoginSenha():
    time.sleep(8)
    print("Preenchendo Usuario")
    cnpj = navegador.find_element_by_id('inputEmail')
    cnpj.clear()
    cnpj.send_keys('douglas.correa@cnseg.org.br')
    print("Preenchendo Senha")
    senha = navegador.find_element_by_id('inputPassword')
    senha.clear()
    senha.send_keys('XXXX')
    time.sleep(8)
    print("Logando....")
    senha.send_keys(Keys.ENTER)
    time.sleep(25)
def seLoga():
    try:
        preencheLoginSenha()
        time.sleep(15)
        navegador.find_element_by_xpath("//*[text()='Sair']")
        print("Se logou corretamente")
    except NoSuchElementException:
        try:
            print ("Entrou no Except, tentando novamente se logar")
            carregaPagina()
            preencheLoginSenha()
            time.sleep(35)
            navegador.find_element_by_xpath("//*[text()='Sair']")
            print ("Se logou corretamente")
        except NoSuchElementException:
            try:
                print ("Entrou no Except, não conseguiu se logar.")
                gravaLogFail()
                mailSend('[Enquadramento] Nao foi possível se logar', 'Enquadramento não logou')
                time.sleep(5)
                navegador.quit()
                sys.exit()
            except:
                navegador.quit()
                sys.exit()


# In[19]:


#Funcao de navegacao até placa simples
def navegaPlaca():
    navegador.get('https://enquadramentoveiculo.cnseg.org.br/home')
    time.sleep(5)
    navegador.find_element_by_xpath("//*[text()='Consulta por Placa']").click()
    time.sleep(5)
    navegador.find_element_by_xpath("//*[text()=' Placa Simples']").click()


# In[20]:


#Consulta a PLACA
def consultaPlaca1():
    print("Consultando Placa")
    time.sleep(2)
    placa = navegador.find_element_by_xpath('//*[@id="conteudo"]/mat-card/form/div/div/input')
    time.sleep(2)
    placa.send_keys('KUP4311')
    time.sleep(2)
    placa.send_keys(Keys.ENTER)
    time.sleep(12)
    navegador.find_element_by_xpath("//*[text()='9BD17164G72820442']")
    print ("Passou no teste, consulta valida.")
def consultaPlaca2():
    print("Consultando Placa")
    time.sleep(2)
    placa = navegador.find_element_by_xpath('//*[@id="conteudo"]/mat-card/form/div/div/input')
    time.sleep(2)
    placa.clear()
    placa.send_keys('LPO4128')
    time.sleep(2)
    placa.send_keys(Keys.ENTER)
    time.sleep(30)
    navegador.find_element_by_xpath("//*[text()='9BFZE55P9A8578019']")
    print ("Passou no teste, consulta valida.")


# In[21]:


## MAIN ##
try:
    carregaPagina()
    seLoga()
    navegaPlaca()
    consultaPlaca1()
    gravaLogPass()
    navegador.quit()
    sys.exit()
except NoSuchElementException:
    try:
        print("Primeiro teste com falha, aguardando 25 segundos para tentar novamente.")
        time.sleep(35)
        navegaPlaca()
        consultaPlaca2()
        gravaLogPass()
        navegador.quit()
        sys.exit()
    except NoSuchElementException:
        try:
            mailSend('[Enquadramento] Nao foi possivel realizar consulta', 'Enquadramento nao foi possivel realizar consulta')
            gravaLogFail()
            navegador.quit()
            sys.exit()
        except:
            navegador.quit()
            sys.exit()
5
