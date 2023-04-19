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


class MedSenior:
    
    def __init__(self, teste = True):
        
        #options = webdriver.ChromeOptions()
        
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options() 
        options.page_load_strategy = 'none'
        
        self.driver = webdriver.Chrome(service=service, options=options)
        if not teste :
            self.driver.minimize_window()
           
        self.interation = Interation(self.driver)
        self.url = "https://ptlmedsenior2.topsaude.com.br/PortalCredenciado"
        self.driver.get(self.url)
        
    def get(self, url):
        self.driver.get(url)    
        return True
    
    def login(self, user, password):
        try:
            time.sleep(1)
            login = Login(self.driver)
            
            #self.skip_login()
            #input('enter')
            
            
            login.set_user('usuario', user, method='id')
            
            
            login.set_password('senha', password,  method='id')
            #if self.interation.locacated()
            
            #self.interation.click_js('//*[@id="login-submit"]')
            
            login.click_button('//*[@id="login-submit"]')
            
            return True

        except Exception as e:
            logging.error(e)
            return False
    
    def click_services(self):
        self.interation.click('//*[@id="LumNav"]/li[2]/a')
        
        
    def click_faturamento(self):
        self.interation.click('//*[@id="prestadorMenuSeguradoPrincipal"]/div/div/div/div/div/div[2]/a')
        
    
    def click_guia_consulta(self):
        self.interation.click('/html/body/div[1]/table[10]/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div/div[3]/p[3]/a')
        
    
    def insert_code(self, value =  '111'):
        for i in range(1,6):
            xpath = f'//*[@id="codigo-beneficiario-{i}"]'
            self.interation.write(xpath, 11)
            
            
        
        
        
        
        
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
            self.get('https://credenciado.MedSenior.com.br/pedidos-autorizacao')
            logging.info('clickado no auttorização previa com sucesso')
            
            return True
        except Exception as e:
            logging.error(e)
         
    
    def click_incluir_pedido(self):
        print('vai clicar')
       
        
        xpath_menu = '//*[@id="sm-16811463678817988-1"]'
        #16811458605225508
        # id="sm-16811470290144385-1"
        try:
            #self.interation.click(xpath_menu)
            
            pass
        except:
            #input('deu erro')
            pass
        
        el = self.interation.element('//*[@id="main-menu"]')
        els = el.find_elements('xpath', '//li')
        for el in els:
            if 'Autorização' in el.get_attribute('outerHTML'):
                el.click()
                #print(el.get_attribute('outerHTML'))
                
        
        js = 'document.querySelector("#sm-16811458605225508-1").mouseover()'
        
        self.driver.execute_script(js)
        
        # self.interation.click_js(xpath_menu)
        # print('clicou')
        
        xpath = '//*[@id="sm-16811448388603662-2"]/li[1]/a'
        self.interation.click(xpath)
        
        
    
    
if __name__ == "__main__":
    sul = MedSenior()
    print(1)
    for i in range(6):
        sul.login('0001852', 'P03340')
        if not sul.driver.current_url == sul.url:
            break
        time.sleep(5)
        
         
    #print(2)
    
    #sul.get('https://ptlmedsenior2.topsaude.com.br/PortalCredenciado/HomePortalCredenciado/Home/AreaLogada')
    sul.click_incluir_pedido()
    #input('enter')
    #print(sul.interation.verify_page('home'))
    #sul.get('https://ptlmedsenior2.topsaude.com.br/PortalCredenciado/HomePortalCredenciado/Home/AreaLogada#PORCRED9_00')
    # sul.click_autorization_previa()
    # sul.insert_CPF('550628703')
    # sul.insert_atendimento('consulta')
    input('enter')