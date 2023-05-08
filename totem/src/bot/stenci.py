import os
import sys
import time
import json
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

#from src.interation.login import Login
#from src.interation import Interation

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
        options.add_argument('--log-level=4')
        
        self.driver = webdriver.Chrome(service=service, options=options)
        if not teste :
            self.driver.minimize_window()
           
        self.i = Interation(self.driver)
        
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
        self.i.click('//*[@id="app"]/section/aside/nav/a[2]')
        self.select_agenda()
        return True
    
    
    def set_client(self, client):
        self.i.write(
            '//*[@id="app"]/section/main/div/div[3]/div/div/div/div[1]/div/input', 
            client)
        
        return True
    
    def client_click(self):
        self.i.click('//*[@id="app"]/section/main/div/div[3]/div/table/tbody/tr/td[3]', time=40)
        
        #self.i.click('//*[@id="modal-appointment"]/div/div[2]/div[2]/div/ul/li[3]/a')
        return True
    
    def select_agenda(self):
        select_element = self.i.element('//*[@id="professional"]')
        select = Select(select_element)
        select.select_by_visible_text('[Todos]')
    
    
    def get_infos(self):
        values = {}
        paths = {
            #'name': '//*[@id="company-name"]',
            #'tel': '//*[@id="phone"]',
            
            'carteira':'//*[@id="appointment-insurance-record"]'   
        }
                       
        for path in paths.keys():
            time.sleep(1)
            el = self.i.element(paths[path]).get_attribute('value')
            
            values[path] = el
        
        select = self.i.element('//*[@id="appointment-professional"]/option[2]').get_attribute('text')
        #select = Select(select)
        values['medico'] = ' '.join(select.split()[:-1])
        
        
        select_element = self.i.element('//*[@id="appointment-insurance"]')
        select = Select(select_element)
        values['convenio'] = select.all_selected_options[0].text
        
        
        return values 
    
    
    def finalizar(self):
        
        self.i.click('//*[@id="modal-appointment"]/div/div[2]/div[2]/div/ul/li[2]/a')
        time.sleep(1)
        
        input_xpath = '//*[@id="expense-name"]'
        self.i.element(input_xpath).clear()
        
        self.i.write(input_xpath, '10101012') 
        self.i.click('//*[@id="expenses"]/div/form/div/div/div/form/div/button')   
        #self.i.click('//*[@id="modal-expenses-appointment"]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]')
        
       
        xpath = "//td[text()='Consulta em Consultório']"
        
        self.i.click(xpath)
        
                #self.i.click(td)
        checkbot = '//*[@id="expenses"]/div/div/div[2]/table/tbody/tr/td[1]/div/label/input'
        self.i.element(checkbot)
        js = """
        let check = document.querySelector("#expenses > div > div > div:nth-child(2) > table > tbody > tr > td:nth-child(1) > div > label > input[type=checkbox]")
        
        if (check.checked == true){ 
        check.checked = false;

            }
       
        check.click()
        """
        self.driver.execute_script(js)
        #input('finalizar')
        #self.i.click(checkbot)
        
        
        self.i.click('//*[@id="div-register-service"]/button', time=30)
        
        self.i.element('//*[@id="referral-service-type"]', time=30)
        
        self.clicks_select_final()
        
        el = '//*[@id="modal-appointment"]/div/div[2]/div[3]/button[3]'
        #//*[@id="modal-appointment"]/div/div[2]/div[3]/button[3]
        self.i.click_js(el, time=40)
        
        logging.info(self.i.element(el).get_attribute('outerHTML'))
        time.sleep(2)
        #js= 'document.querySelector("#modal-appointment > div > div.modal-container > div.modal-footer > button.btn.btn-gray.mr-2").click()'
        #self.driver.execute_script(js)
        #input('finalizar')
        #self.i.key(input_xpath, Keys.DOWN)
        #input('finalizar')
        #self.i.key(input_xpath, 'enter')
        
        
        
        
        
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
            self.i.click(i)
            print('clicou')'''
            
        #self.driver.execute_script()
            
        #self.i.click('//*[@id="expenses"]/div/div/div[2]/table/tbody/tr/td[1]/div/label/input')
        #self.i.write('//*[@id="expense-name"]','consulta' )
        time.sleep(1)
        #self.i.click('//*[@id="expenses"]/div/form/div/div/div/form/div/button')                              
        time.sleep(1)
        
        #self.i.click('//*[@id="modal-expenses-appointment"]/div/div[2]/div[2]/table/tbody/tr[2]')
        
    def clicks_select_final(self):
        clicks = ['//*[@id="referral-service-type"]/option[2]',
         '//*[@id="consultation-type"]/option[2]',
         '//*[@id="referral-type"]/option[2]'
         ]
        
        for el in clicks:
            self.i.click(el,  time=40)
        
        el = '//*[@id="modal-particular-account"]/div/div[2]/div[3]/button[1]'
        self.i.click_js(el,  time=40)
        time.sleep(2)
        
        
    def extrair_medicos(self):	
        host = 'https://stenci.app'
        self.driver.get('https://stenci.app/clinical/professionals')
        medicos = self.i.elements('//*[@id="app"]/section/main/div/div[2]/div[2]/table/tbody/tr/td/a')
        
        all_medicos = []
        links = []
        for medico in medicos:
                links.append(medico.get_attribute('href'))
                
        for medico in links:
                try:
                    self.driver.get(medico)

                    #time.sleep(2)
                    
                    
                    name = self.i.element('//*[@id="company-name"]').get_attribute('value')
                    cpf = self.i.element('//*[@id="company-cpf"]').get_attribute('value')
                    conselho = self.i.element('//*[@id="professional-council"]').get_attribute('value')
                    uf = self.i.element('//*[@id="professional-council-state"]').get_attribute('value')
                    
                    especialidade = self.i.element('//*[@id="professional"]/div[5]/div[5]/table/tbody/tr[2]/td[1]').text
                    name_especialidade = self.i.element('//*[@id="professional"]/div[5]/div[5]/table/tbody/tr[2]/td[2]').text
                    
                    medico_dict = {
                        'name': name,
                        'cpf': cpf,
                        'especialidade': especialidade,
                        'conselho':conselho,
                        'uf':uf,
                        'name_especialidade': name_especialidade
                    }
                    
                    all_medicos.append(medico_dict)
                    self.driver.get('https://stenci.app/clinical/professionals')
                    time.sleep(2)
            
                except:
                    print(medico)
                
            
        
        
        with open('medicos.json', 'w') as f:
            json.dump(all_medicos, f)
            
        
        
        
            
            
            
        
        
        
    
if __name__ == '__main__':
     
    i = time.time()
    
    s = Stenci(True)
    #time.sleep(20)
    
    #input('ta parado')
    login = s.login("74655523549", 'crm1234')
    time.sleep(2
               )
    
    #s.click_agenda()
    s.extrair_medicos()
    
    
    #s.set_client('Ana Paula Dimitrow Gracia Pereira Portugal')
    #input('ta parado')
    
    #s.client_click()
    
    #a = s.get_infos()
    #print(a)
     
            
    #s.finalizar()

    f = time.time()
    
    print(f"demorou {f - i} segundos para concluir")
    
    input('fechou')
        
    