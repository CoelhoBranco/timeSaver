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
        self.url = "https://paranaclinicas.saudi.com.br/saudi/welcome.do?task=abreLogin"
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
            
            
            login.set_user('/html/body/table[2]/tbody/tr/td/form/table/tbody/tr[8]/td/table/tbody/tr[1]/td[2]/input', user)
            
            
            login.set_password('senha', password,  method='id')
            #if self.interation.locacated()
            
            #self.interation.click_js('//*[@id="login-submit"]')
            
            login.click_button('//*[@id="btn_enviar"]')
            
            return True

        except Exception as e:
            logging.error(e)
            return False
    
    def click_services(self):
        print('iniciou o click')
        #input('inicar sistema')
        el = self.interation.element('topFrame', method='id')
        self.driver.switch_to.frame(el)
        print('iniciou o iframe')
    
        self.interation.click('/html/body/div[1]', method='xpath')
        #print('achou o elemento')
        self.driver.switch_to.default_content()
        
        
       
    
    def click_guia_consulta(self):
        el = self.interation.element('frameConteudo', method='id')
        self.driver.switch_to.frame(el)
        
        self.interation.click('//*[@id="5485"]/div[1]/span')
        self.interation.click('//*[@id="5486"]/span/a')
        
    
    def insert_code(self, value =  '111'):
    
        xpath = f'//*[@id="tissBeneficiarioVO.numCarteira"]'
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
    for i in range(1):
        sul.login('12553_atend', 'saudi@p')
        if not sul.driver.current_url == sul.url:
            break
        #time.sleep(5)
        
         
    #print(2)
    
    #sul.get('https://ptlmedsenior2.topsaude.com.br/PortalCredenciado/HomePortalCredenciado/Home/AreaLogada')
    sul.click_services()
    sul.click_guia_consulta()
    sul.insert_code()
    #input('enter')
    #print(sul.interation.verify_page('home'))
    #sul.get('https://ptlmedsenior2.topsaude.com.br/PortalCredenciado/HomePortalCredenciado/Home/AreaLogada#PORCRED9_00')
    # sul.click_autorization_previa()
    # sul.insert_CPF('550628703')
    # sul.insert_atendimento('consulta')
    input('enter')