import sys, os
import requests
import json
import logging
from unidecode import unidecode
from src.bot.unimed import Unimed
from src.bot.stenci import Stenci

        
logging.basicConfig(filename='logs.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S', level=logging.INFO, encoding="UTF-8")

id = 1
empresa = 'Unimed'
host = 'timesaver.com.br'

paciente = False

def get_password(empresa):
    empresa = empresa.lower()
    url = f'http://{host}/controller/read/{empresa}?id={id}'
    print(url)
    r = requests.get(url).json()['result'][0]
    print('vai vir o print do json')
    print(r)
    #r
    return {'user' : r['user'], 'password' : r['password'] }

def status(code):
    with open('status.json', 'w') as f:
        f.write(json.dumps({'code': code}))


def exec(paciente):
    try:
        for _ in range(2):
            status(100)
            stenci = Stenci(teste=True)
        
            senhas = get_password('Stenci')
            stenci.login(senhas['user'], senhas['password'])

            stenci.click_agenda()

            stenci.set_client(paciente)

            stenci.client_click()
            
            for _ in range(5):
                data = stenci.get_infos() 
                if data['carteira']:
                    break
                
            print(data)   
            result = unimed(data['carteira'], data['medico'])
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
            print(f'carteira {carteira}')
            u = Unimed(teste=True)
            #('terminou de carregar') 
            senhas = get_password('Unimed')
            u.login(senhas['user'], senhas['password'])
            #('fechar')
            u.page_exec()
            #('fechar')
            #print(u.driver.current_url)
            u.select(medico)

            u.set_beneficiary(carteira)
            u.click_send()
            #('aperte enter')
            try:
                u.driver.get('https://autorizador.unimedcuritiba.com.br/DigitarConsulta32.aspx')
                u.set_value(medico)
            except Exception as e:
                print(e)
            u.click_final()
            
                         
            return u.verify_conclusion()
            
                        
        except Exception as e:
            logging.exception(e)
            continue


if len(sys.argv) > 1:
    exec(sys.argv[1])
    #os.system('py bots.py' + )

    

'''
s = Stenci()
    #time.sleep(20)
    #('ta parado')
s.login("74655523549", 'crm1234')

s.click_agenda()

s.set_client('Maria Cecília da Rocha')

s.client_click()

s.get_infos()

'''
