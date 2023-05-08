import sys, os
import requests
import json

import time
from urllib.parse import quote
from unidecode import unidecode
from src.bot.unimed import Unimed
from src.bot.stenci import Stenci
from src.bot.amil import Amil
from src.bot.medsenior import MedSenior
from src.bot.my_logger import get_logger

logging = get_logger()

id = 1
empresa = 'Unimed'
host = 'timesaver.com.br'

paciente = False

def get_password(empresa):
    empresa = empresa.lower()

    url = f'https://{host}/controller/read/senhas?empresa={empresa}&id={id}'
    print(url)
    r = requests.get(url).json()['result'][0]
    print('vai vir o print do json')
    print(r)
    #r
    return {'user' : r['user'], 'password' : r['password'] }

def get_medico(medico):
    medico = quote(medico)
    url = f'https://{host}/controller/read/medicos?medico={medico}&id={id}'
    logging.info(url)
    r = requests.get(url).json()['result'][0]
    return {"name":r['name'], "cbo":r['cbo']}

    

def status(code):
    with open('status.json', 'w') as f:
        f.write(json.dumps({'code': code}))
        
def get_token():
    while True:
        with open('config/token.json', 'r') as f:
            token = f.read()
            token = json.loads(token)
        
        if token['token']:
            return token['token']
        
        time.sleep(4)
        
def zerar_token():
    with open('config/token.json', 'w') as f:
            f.write(json.dumps({'token': None}))
        

def start_stenci(paciente):
    global stenci
     
    stenci = Stenci(teste=True)

    senhas = get_password('Stenci')
    stenci.login(senhas['user'], senhas['password'])

    stenci.click_agenda()

    stenci.set_client(paciente)

    stenci.client_click()
    return stenci


def escolher_convenio(data):
    result = False
    
    convenio = data['convenio']
    logging.info(f'convenio utilizado:{convenio}')
    
    
    
    if convenio == "Unimed Curitiba":
        result = unimed(data['carteira'], data['medico'])
        
    if convenio == "Amil (Planos)":
        result = exec_amil(data)
        
    
    if convenio == "MedSênior":
        result = exec_medSenior(data)
    
    if result:
        status(200)
    else:
        status(300)
        
    return result
        
        
            

def exec_amil(data):
    
    senha = get_password('Amil (Planos)')
    {'name': 'Bruna Rafaela de Deus Lima', 'cbo': '225250'}
    
    medico = get_medico(data['medico'])
    
    amil = Amil(senha['user'], senha['password'])

    amil.click_autorization_previa()
    amil.insert_CPF(data['carteira'])
    amil.insert_atendimento('consulta')
    
    amil.insert_data()    
    amil.inserir_solicitante(medico['name'], medico['cbo'])
    amil.inserir_servico()
    amil.click_incluir()
    
    status(400)
    
    token = get_token()
    zerar_token()
    amil.inserir_token(token)
    
    
    return amil.verify_token()
       
def exec_medSenior(data):
    
    senha = get_password('MedSênior')
    med = MedSenior(senha['user'], senha['password'])    
    med.inserir_beneficiario(data['carteira'])
    med.inserir_cel('2199999999')
    result = med.final()

    return result
 

        
        
   

def exec(paciente):
    status(100)
    try:
        for _ in range(2):
            
            start_stenci(paciente)
            
            for _ in range(5):
                data = stenci.get_infos() 
                print(data)
                if data['carteira']:
                    break
                
               
            result = escolher_convenio(data)
            input("Enter")
            for _ in range(2):
                try:
                    if result == False:
                        status(300)
                    else:
                        
                        stenci.finalizar()
                        
                        stenci.driver.close()
                    status(200)
                    return True
                
                except Exception as e:
                    logging.exception(e)
    
    except Exception as e:
        stenci.driver.close()
        logging.exception(e)
        status(300)

def unimed(carteira, medico):
    medico = unidecode(medico)
    for _ in range(3):
        try:
                        
            senhas = get_password('Unimed')
            u = Unimed(senhas['user'], senhas['password'], teste=True)
            
            u.select(medico)

            u.set_beneficiary(carteira)
                       
            try:
                u.set_value(medico)
            except Exception as e:
                logging.error(e)
            u.click_final()
                                     
            return u.verify_conclusion()
                                    
        except Exception as e:
            logging.exception(e)
            continue


if len(sys.argv) > 1:
    print(sys.argv[1])
    exec(sys.argv[1])
    #get_medico('Marcos de abreu bonardi')
    #print(sys.argv)
   




