import time
import os
import codecs
import math
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
from bs4 import BeautifulSoup as bs
import json
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
#firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

service=FirefoxService(GeckoDriverManager().install())
#service=(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php/buscador-primo.html"
driver.get(url)

print("Iniciando extração de dados!")

morepages = True
relevancia = 1
lista_resultados = []
lista_referencias = []
lista_autores = []
lista_autores_instituicao = []
while (morepages):
    tabela = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#searchResultsContainer"))
    )

    linhas = tabela.find_elements(By.CSS_SELECTOR, ".list-item-wrapper")

    for linha in linhas:
        try:
            link = linha.find_elements(By.CSS_SELECTOR, "a")[1]
        except:
            pass

        try:
            título = link.get_attribute("innerText")
        except:
            título = ""

        try:
            url = link.get_attribute("href")
        except:
            url = ""

        try:
            autor = linha.find_element(By.CSS_SELECTOR,
                                        "span[data-field-selector=creator]")

            autor = autor.get_attribute("innerText")
        except:
            autor = ""

        try:
            publicação = linha.find_element(By.CSS_SELECTOR,
                                            "span[data-field-selector=source]")

            publicação = publicação.get_attribute("innerText")
        except:
            publicação = ""

        try:
            descrição = linha.find_element(By.CSS_SELECTOR,
                                            "span[data-field-selector=description]")

            descrição = descrição.get_attribute("innerText")
        except:
            descrição = ""

        lista_resultados.append(
            [relevancia, título, url, autor, publicação, descrição])
        relevancia += 1

        autor_separado = autor.split(";")
        for autor_ind in autor_separado:
            autor_ind = autor_ind.lstrip()
            if not autor_ind:
                continue
            else:
                lista_autores.append([título, autor_ind, "", ""])

    referencias_buttons = tabela.find_elements(
        By.CSS_SELECTOR, "[md-svg-icon='primo-ui:citing']")

    i = 0

    for button in referencias_buttons:
        # try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#searchElementsWrapper"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".list-item-primary-content"))
        )
        WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, f"[md-svg-icon=\'primo-ui:citing\']"))
        )
        time.sleep(4)
        try:
            driver.execute_script(
                f'document.querySelectorAll("[md-svg-icon=\'primo-ui:citing\']")[{i}].click()')
            i += 1
            # button.click()\\

            referencias_button_close = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".back-button"))
            )

            referencias = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".result-item-details .item-title"))
            )

            referencias = driver.find_elements(
                By.CSS_SELECTOR, ".result-item-details .item-title")
            for referencia in referencias:
                lista_referencias.append([título, referencia.get_attribute("innerText")])

            time.sleep(2)
            driver.execute_script(f'window.history.go(-1)')

        except:
            time.sleep(2)
            driver.execute_script(f'window.history.go(-1)')
            # referencias = []

        finally:
            # referencias_button_close.click()
            # driver.execute_script(f'document.querySelector(".back-button").click()')
            continue

    try:
        proximo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.counter-next:not(.ng-hide)')))
        proximo.click()
        morepages = True
    except:
        morepages = False

    for autor in lista_autores:
        try:
            url_orcid = f'https://orcid.org/orcid-search/search?searchQuery={autor[1]}'

            driver.get(url_orcid)

            autor_instituicao = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".ng-star-inserted td:nth-child(5)"))
            )

            autor_instituicao = linha.find_element(By.CSS_SELECTOR,
                                                   ".ng-star-inserted td:nth-child(5)")

            autor_instituicao = autor_instituicao.get_attribute("innerText")

            autor[2] = autor_instituicao
        except:
            continue
        finally:
            lista_autores_instituicao.append(autor)

    df = pd.DataFrame(lista_resultados, columns=[
        "Relevância", "Título", "Link", "Autor", "Publicação", "Descrição"])

    df_referencias = pd.DataFrame(lista_referencias, columns=[
        "Título", "Referência"])

    df_autores = pd.DataFrame(lista_autores_instituicao, columns=[
        "Título", "Autor", "Instituição", "País"])

    #orcid = Orcid().pesquisar()

    #df = orcid.busca(df)

    

    '''try:
            resultadosquantidade = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='mainResults']/prm-search-result-tool-bar/div/md-toolbar/div[2]/span[2]"))
            )

            resultadosquantidade = resultadosquantidade.get_attribute(
                "innerHTML")

            resultadosquantidade = re.sub('[^0-9]', '', resultadosquantidade)

            resultadosquantidade = int(resultadosquantidade)
        except:
            resultadosquantidade = None
            print("Erro ao encontrar resultados! Tente novamente mais tarde!")
        else:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("Resultados encontrados: "+str(resultadosquantidade))

            pages = math.floor(resultadosquantidade/10)
            print("Número de páginas: "+str(pages))

            lista_resultados = []

            for page in range(pages):
                print("Página: "+str(page)+" de "+str(pages) )
                tabela = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//*[@id='searchResultsContainer']"))
                )



                linhas = tabela.find_elements_by_xpath("//div[@clas='list-item']")
                print(linhas)

                relevancia = 1

                for linha in linhas:
                    link = linha.find_element_by_xpath("//h3/a")

                    2

                    lista_resultados.append(
                        [relevancia, título, url, autor, publicação, descrição])
                    relevancia += 1

                try:
                    proximo = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//a[@ng-click="$ctrl.getNextPage($event)"]')))
                    proximo.click()
                except:
                    pass

            df = pd.DataFrame(lista_resultados, columns=[
                "Relevância", "Título", "Link", "Autor", "Publicação", "Descrição"])

            orcid = Orcid().pesquisar()

            df = orcid.busca(df)

            driver.quit()

            açãoSalvamento()'''
