import os
import sys
import time
import logging
import datetime

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import logging as log

os.environ['WDM_LOG'] = str(log.NOTSET)


sys.path.append(os.getcwd())

from src.interation.login import Login

from src.interation import Interation

<<<<<<< HEAD
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
=======

>>>>>>> 008eacfa0f8bee74eb598b5a3ad3a27f6c02d807


class Imprimir:
    
    def __init__(self,teste = True):
        
        #options = webdriver.ChromeOptions()
        
<<<<<<< HEAD
        if False:
            service = Service(executable_path=ChromeDriverManager().install())
            options = Options() 
            options.page_load_strategy = 'normal'
            options.add_argument('--log-level=4')
            self.driver = webdriver.Chrome(service=service, options=options)
        
        #service=FirefoxService(GeckoDriverManager().install())
        path = os.getcwd() + '/geckodriver.exe'
        #path = GeckoDriverManager().install()
        try:
            service=FirefoxService(os.getcwd() + '/geckodriver.exe')
            self.driver = webdriver.Firefox(service=service)        
        except:
            pass
        print('1')
               
=======
        
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options() 
        options.page_load_strategy = 'normal'
        options.add_argument('--log-level=4')
        self.driver = webdriver.Chrome(service=service, options=options)
        
     
>>>>>>> 008eacfa0f8bee74eb598b5a3ad3a27f6c02d807
        if not teste :
            self.driver.minimize_window()
           
        self.i = Interation(self.driver)
<<<<<<< HEAD
        print('carregou a pagina')
        self.driver.get("http://localhost:5000/teste")
=======
        
        self.driver.get("http://127.0.0.1:5000/teste")
>>>>>>> 008eacfa0f8bee74eb598b5a3ad3a27f6c02d807
        print('carregou a pagina')
        
    
    def click(self):
        js = '''
        
        setTimeout(function() {
  document.querySelector("body > print-preview-app").shadowRoot.querySelector("#sidebar").shadowRoot.querySelector("print-preview-button-strip").shadowRoot.querySelector("div > cr-button.action-button").click()
}, 10000); // 10000 milisegundos = 10 segundos
        '''
        #self.driver.execute_async_script(js)
<<<<<<< HEAD
        print('click em imprimir')
        self.i.click('//*[@id="imprimir"]')
        #self.i.click_js('//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]')
        self.driver.window_handles
        print('print da janelas')
        print(self.driver.window_handles)
=======
        
        self.i.click('//*[@id="imprimir"]')
        self.i.click_js('//*[@id="sidebar"]//print-preview-button-strip//div/cr-button[1]')
        self.driver.window_handles[-1]
>>>>>>> 008eacfa0f8bee74eb598b5a3ad3a27f6c02d807
        print('print das janelas')
        
    def mudar_janela(self):
        # Mude o foco para a janela de impressão
        print('print das janelas')
        self.driver.window_handles[-1]
        self.driver.switch_to.window(self.driver.window_handles[-1])

        print('print das janelas')
        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        
if __name__ == '__main__':
    i = Imprimir()
    i.click()
    print('print')
    i.mudar_janela()
    input('enter')
    