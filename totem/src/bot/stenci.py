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
logging.basicConfig(filename='logs.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S', level=logging.INFO, encoding="UTF-8")


class Stenci:
    
    def __init__(self, teste = False):
        
        #options = webdriver.ChromeOptions()
        
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options() 
        options.page_load_strategy = 'none'
        
        self.driver = webdriver.Chrome(service=service, options=options)
        if not teste :
            self.driver.minimize_window()
           
        self.interation = Interation(self.driver)
        
        self.driver.get("https://stenci.app")
        #options.page_load_strategy = 'none'
        
    
    def login(self, user, password):
        try:
            login = Login(self.driver)
            
            login.set_user('//*[@id="username"]', user)
            
            login.set_password('//*[@id="password"]', password)
            
            login.click_button('/html/body/div[1]/div[3]/form/button')
            
            return True

        except:
            return False
    
    
    def click_agenda(self):
        self.interation.click('//*[@id="app"]/section/aside/nav/a[2]')
        return True
    
    
    def set_client(self, client):
        self.interation.write(
            '//*[@id="app"]/section/main/div/div[3]/div/div/div/div[1]/div/input', 
            client)
        
        return True
    
    def client_click(self):
        self.interation.click('//*[@id="app"]/section/main/div/div[3]/div/table/tbody/tr/td[3]', time=40)
        
        #self.interation.click('//*[@id="modal-appointment"]/div/div[2]/div[2]/div/ul/li[3]/a')
        return True
    
    
    def get_infos(self):
        values = {}
        paths = {
            #'name': '//*[@id="company-name"]',
            #'tel': '//*[@id="phone"]',
            
            'carteira':'//*[@id="appointment-insurance-record"]'   
        }
                       
        for path in paths.keys():
            time.sleep(1)
            el = self.interation.element(paths[path]).get_attribute('value')
            
            values[path] = el
        
        select = self.interation.element('//*[@id="appointment-professional"]/option[2]').get_attribute('text')
        #select = Select(select)
        values['medico'] = ' '.join(select.split()[:-1])
        
        
        
        return values 
    
    
    def finalizar(self, ):
        
        self.interation.click('//*[@id="modal-appointment"]/div/div[2]/div[2]/div/ul/li[2]/a')
        #time.sleep(1)
        
        input_xpath = '//*[@id="expense-name"]'
        self.interation.element(input_xpath).clear()
        
        self.interation.write(input_xpath, '10101012') 
        self.interation.click('//*[@id="expenses"]/div/form/div/div/div/form/div/button')   
        #self.interation.click('//*[@id="modal-expenses-appointment"]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]')
        
       
        xpath = "//td[text()='Consulta em Consultório']"
        
        self.interation.click(xpath)
        
                #self.interation.click(td)
        checkbot = '//*[@id="expenses"]/div/div/div[2]/table/tbody/tr/td[1]/div/label/input'
        self.interation.element(checkbot)
        js = """
        let check = document.querySelector("#expenses > div > div > div:nth-child(2) > table > tbody > tr > td:nth-child(1) > div > label > input[type=checkbox]")
        
        if (check.checked == true){ 
        check.checked = false;

            }
       
        check.click()
        """
        self.driver.execute_script(js)
        #input('finalizar')
        #self.interation.click(checkbot)
        
        
        self.interation.click('//*[@id="div-register-service"]/button', time=30)
        
        self.interation.element('//*[@id="referral-service-type"]', time=30)
        
        self.clicks_select_final()
        
        el = '//*[@id="modal-appointment"]/div/div[2]/div[3]/button[3]'
        self.interation.click(el, time=40)
        js= 'document.querySelector("#modal-appointment > div > div.modal-container > div.modal-footer > button.btn.btn-gray.mr-2").click()'
        #self.driver.execute_script(js)
        #input('finalizar')
        #self.interation.key(input_xpath, Keys.DOWN)
        #input('finalizar')
        #self.interation.key(input_xpath, 'enter')
        
        
        
        
        '''jsS = ['document.querySelector("#expenses > div > div > div:nth-child(2) > table > tbody > tr > td:nth-child(1) > div > label > input[type=checkbox]").checked = true;',
              'document.querySelector("#div-register-service > button").disabled = false;',
              'document.querySelector("#div-register-service > button").click()'
              
              ]
        
        for js in jsS:
            try:
                time.sleep(0.5)
                self.driver.execute_script(js)
            except Exception as e:
                print(e)
                print(js)
        
        js_list = ['document.querySelector("#referral-service-type > option:nth-child(2)").selected = true;',              
                   'document.querySelector("#consultation-type").disabled = false;',
                    'document.querySelector("#consultation-type > option:nth-child(2)").selected = true;',
                    'document.querySelector("#consultation-type > option:nth-child(2)").selected = true;'
                    ]
        
        for js in js_list:
            try:
                time.sleep(1)
                self.driver.execute_script(js)
            except Exception as e:
                
                print(js)
                print(e)
            
        #//*[@id="consultation-type"]/option[2]
        xpaths = ['//*[@id="consultation-type"]/option[2]',
                  '//*[@id="referral-type"]/option[2]']
        for i in xpaths:
            self.interation.click(i)
            print('clicou')'''
            
        #self.driver.execute_script()
            
        #self.interation.click('//*[@id="expenses"]/div/div/div[2]/table/tbody/tr/td[1]/div/label/input')
        #self.interation.write('//*[@id="expense-name"]','consulta' )
        time.sleep(1)
        #self.interation.click('//*[@id="expenses"]/div/form/div/div/div/form/div/button')                              
        time.sleep(1)
        
        #self.interation.click('//*[@id="modal-expenses-appointment"]/div/div[2]/div[2]/table/tbody/tr[2]')
        
    def clicks_select_final(self):
        clicks = ['//*[@id="referral-service-type"]/option[2]',
         '//*[@id="consultation-type"]/option[2]',
         '//*[@id="referral-type"]/option[2]'
         ]
        
        for el in clicks:
            self.interation.click(el,  time=40)
        
        el = '//*[@id="modal-particular-account"]/div/div[2]/div[3]/button[1]'
        self.interation.click(el,  time=40)
    
if __name__ == '__main__':
     
    i = time.time()
    
    s = Stenci(True)
    #time.sleep(20)
    #input('ta parado')
    
    for i in range(3):
        login = s.login("74655523549", 'crm1234')
        if login:
            break
    
    s.click_agenda()
    
    s.set_client('joao teste')
    #input('ta parado')
    
    s.client_click()
    
    a = s.get_infos()
    print(a)
     
            
    s.finalizar()

    f = time.time()
    
    print(f"demorou {f - i} segundos para concluir")
    
    input('fechou')
        
    