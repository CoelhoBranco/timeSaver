from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait



class Interation:
    
    
    def __init__(self, driver):
        
        self.driver = driver

    
    def write(self, tag:str, message:str, method:str='xpath', time:int=15):
            
            WebDriverWait(self.driver, time).until(
                    EC.element_to_be_clickable((method, tag)))
            element = self.driver.find_element(method, tag)
                        
            element.send_keys(str(message))
            return True
                        

    def click(self, tag:str, method = 'xpath', time=10):
            WebDriverWait(self.driver, time).until(
                    EC.element_to_be_clickable((method, tag)))
            element = self.driver.find_element(method, tag)
                
            element.click()
            return True
        
    
    def key(self, tag:str, key = 'enter',  time:int=15, method:str='xpath'):
                                
        WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((method, tag)))
        element = self.driver.find_element(method, tag)
                            
        if key == 'enter':
            element.send_keys(Keys.ENTER)

        elif key == 'esc':
            element.send_keys(Keys.ESCAPE)
            
        elif key == 'home':
            element.send_keys(Keys.HOME)
            
        else:
            element.send_keys(key)
            
        
        return True
    
    
    def element(self, tag:str, time:int=15, method:str='xpath'):
        
        WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((method, tag)))
        element = self.driver.find_element(method, tag)
        
        return element