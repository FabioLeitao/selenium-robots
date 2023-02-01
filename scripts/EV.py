#!/usr/bin/env python3
# coding: utf-8

# In[12]:


import time, os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pathlib import Path
from shutil import move
from selenium.common.exceptions import NoSuchElementException
from sendmail import *

# In[13]:

### DEBUG ### ON or OFF
debug = "ON"

#Variaveis Globais
rootPath = "c:\Python"
driverPath = os.getcwd()+'\\chromedriver.exe'
homeDir = str(Path.home())

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
    options = Options()
    options.add_argument("--headless")
    options.add_argument('window-size=1920x1080')
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
        time.sleep(10)
        navegador.find_element_by_id('inputPassword')
        print ("Carregada!")
        return
    except NoSuchElementException:
        try:
            print ("Entrou no Except, tentando novamente")
            time.sleep(15)
            navegador.get('https://enquadramentoveiculo.cnseg.org.br')
            time.sleep(10)
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
    print("Preenchendo Usuario")
    cnpj = navegador.find_element_by_id('inputEmail')
    cnpj.clear()
    cnpj.send_keys('xxxxx')
    print("Preenchendo Senha")
    senha = navegador.find_element_by_id('inputPassword')
    senha.clear()
    senha.send_keys('xxxx')
    time.sleep(2)
    print("Logando....")
    senha.send_keys(Keys.ENTER)
    time.sleep(15)
def seLoga():
    try:
        preencheLoginSenha()
        time.sleep(5)
        navegador.find_element_by_xpath("//*[text()='Sair']")
        print("Se logou corretamente")
    except NoSuchElementException:
        try:
            print ("Entrou no Except, tentando novamente se logar")
            preencheLoginSenha()
            time.sleep(5)
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
    time.sleep(3)
    navegador.find_element_by_xpath("//*[text()='Consulta por Placa']").click()
    time.sleep(3)
    navegador.find_element_by_xpath("//*[text()=' Placa Simples']").click()


# In[20]:


#Consulta a PLACA
def consultaPlaca1():
    print("Consultando Placa")
    time.sleep(2)
    placa = navegador.find_element_by_xpath('//*[@id="conteudo"]/mat-card/form/div/div/input')
    time.sleep(2)
    placa.send_keys('KAH2121')
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
        time.sleep(25)
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

