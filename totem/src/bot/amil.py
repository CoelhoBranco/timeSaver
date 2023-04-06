import os
import sys
import time
import logging

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


sys.path.append(os.getcwd())

from src.interation.login import Login

from src.interation import Interation


class Amil:
    
    def __init__(self, teste = True):
        
        #options = webdriver.ChromeOptions()
        
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options() 
        options.page_load_strategy = 'none'
        
        self.driver = webdriver.Chrome(service=service, options=options)
        if not teste :
            self.driver.minimize_window()
           
        self.interation = Interation(self.driver)
        
        self.driver.get("https://credenciado.amil.com.br/login")
        
    def get(self, url):
        self.driver.get(url)    
        return True
    
    def login(self, user, password):
        try:
            login = Login(self.driver)
            
            #self.skip_login()
            #input('enter')
            login.set_user('//*[@id="login-usuario"]', user)
            
            
            login.set_password('//*[@id="login-senha"]', password)
            #if self.interation.locacated()
            
            self.interation.click_js('/html/body/as-main-app/as-login-container/div[1]/div/as-login/div[2]/form/fieldset/button')
            print('clickou')
            #login.click_button('/html/body/as-main-app/as-login-container/div[1]/div/as-login/div[2]/form/fieldset/button')
            
            return True

        except Exception as e:
            logging.error(e)
            return False
    
    def skip_login(self):
        try:
            self.interation.click("finalizar-walktour",method='id', time=5)
        except:
            print('não encontrado')
            pass
        
    def insert_CPF(self, value =  '111'):
        xpath = '//*[@id="NaN"]'
        self.interation.locacated(xpath)
        self.interation.write_js('#NaN', value)
        self.interation.click(xpath)
        self.driver.execute_script('document.querySelector("#undefined > as-input-float-label > div.input-float-label > button").disabled = false;')
        #self.driver.execute_script('document.querySelector("#undefined > as-input-float-label > div.input-float-label > button").click();')
        self.interation.click('//*[@id="undefined"]/as-input-float-label/div[1]/button')
        return True
    
    
    def insert_atendimento(self, value):
        xpath = '//*[@id="inclusao-consulta-pedido"]/section/div/div/section/div[2]/as-tipo-pedido-autocomplete/div/div/input'
        self.interation.locacated(xpath)
        self.interation.write(xpath, value)
        #
        # self.interation.write_js('#inclusao-consulta-pedido > section > div > div > section > div.tipo-pedido > as-tipo-pedido-autocomplete > div > div > input', value)
        
        return True
    
    
    def click_autorization_previa(self):
        try:
            self.interation.element('//*[@id="menu-usuario"]/as-item-menu[3]/li/a')
            self.get('https://credenciado.amil.com.br/pedidos-autorizacao')
            logging.info('clickado no auttorização previa com sucesso')
            
            return True
        except Exception as e:
            logging.error(e)
         
        
        
    
    
if __name__ == "__main__":
    amil = Amil()
    print(1)
    amil.login('10604456', '@1200procto')
    print(2)
    #input('enter')
    #print(amil.interation.verify_page('home'))
    #amil.get('https://credenciado.amil.com.br/pedidos-autorizacao')
    amil.click_autorization_previa()
    amil.insert_CPF('550628703')
    amil.insert_atendimento('consulta')
    input('enter')