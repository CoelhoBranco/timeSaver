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
from webdriver_manager.core.logger import __logger as wdm_logger
import logging

os.environ['WDM_LOG'] = str(logging.NOTSET)


class Capes_Scraping:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Iniciando programa...\n")
        chrome_driver_path = "./chromedriver.exe"
        firefox_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        url = "https://www-periodicos-capes-gov-br.ezl.periodicos.capes.gov.br/index.php/buscador-primo.html"

        #print("Rodar em modo silencioso:")
        #print("1 - SIM, recomendado, mais rápido!")
        #print("2 - não, NÃO RECOMENDADO, use só para fins didáticos!")
        #print("\n")
        #self.driveroptions = FirefoxOptions()
        #caps = DesiredCapabilities().FIREFOX
        self.driveroptions = Options()
        caps = DesiredCapabilities().CHROME
        self.driveroptions.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        #caps = DesiredCapabilities().FIREFOX
        caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "normal"  #  complete
        caps["pageLoadStrategy"] = "eager"  # interactive
        #caps["pageLoadStrategy"] = "none"
        #self.driver = webdriver.Firefox(desired_capabilities=caps, executable_path=firefox_driver_path, options=self.driveroptions)
        #self.driver = webdriver.Chrome(desired_capabilities=caps, executable_path=chrome_driver_path, options=self.driveroptions)
        #self.driver = webdriver.Chrome(chrome_driver_path, options=self.driveroptions)
        self.driver = firefox_driver;
        self.driver.get(url)

        print("Programa iniciado!")
        iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='busca_primo']"))
            )
        self.driver.switch_to.frame(iframe)
        input("Realize a busca e tecle enter para continuar.")
        self.save()

        '''try:
            busca_avançada_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@class='switch-to-advanced']"))
            )

            webdriver.ActionChains(self.driver).move_to_element(
                busca_avançada_button).click(busca_avançada_button).perform()
        except:
            print("Erro ao iniciar programa!")
        else:
            self.revisãoporpares = False
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//iframe[@name='metabusca']"))
            )
            self.driver.switch_to.frame(iframe)
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa iniciado!")
            self.açãoPré()'''

    def açãoPré(self):
        print("\n")
        print("_____________________________")
        print("Opções:")
        print("1 - Adicionar palavras de busca. (máx: 2)")
        print("2 - Adicionar data inicial.")
        print("3 - Adicionar data final.")
        print("4 - Realizar busca.")
        print("5 - Fechar programa.")
        print("_____________________________")
        print("\n")
        ações = {
            1: self.addPalavra,
            2: self.addDataInicial,
            3: self.addDataFinal,
            4: self.buscar,
            5: exit
        }
        while True:
            try:
                ação = int(input("Digite a opção desejada: "))
                ação = ações[ação]
            except:
                print("Opção inválida!")
                print("\n")
                continue
            else:
                break

        print("\n")
        #os.system('cls' if os.name == 'nt' else 'clear')
        ação()

    def addPalavra(self):
        self.palavras = []
        self.palavras.append(input("Digite a palavra 1: "))
        self.palavras.append(input("Digite a palavra 2: "))

        try:
            palavra1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input_freeText0"))
            )

            palavra2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "input_freeText1"))
            )

            palavra1.clear()
            palavra1.send_keys(self.palavras[0])
            palavra2.clear()
            palavra2.send_keys(self.palavras[1])
        except Exception as error:
            print("Erro ao adicionar palavras, tente novamente!")
            print(error)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Palavras adicionadas!")
            for palavra in self.palavras:
                print(palavra)
        finally:
            self.açãoPré()

    def addDataInicial(self):
        while True:
            data = input("Digite a data (dd/mm/aaaa): ")
            os.system('cls' if os.name == 'nt' else 'clear')
            datasplit = data.split("/")

            if len(datasplit) == 3:
                try:
                    datasplit[0] = int(datasplit[0])
                    datasplit[1] = int(datasplit[1])
                    datasplit[2] = int(datasplit[2])

                    if datasplit[0] > 0 and datasplit[0] <= 31 and datasplit[1] > 0 and datasplit[1] <= 12:
                        self.datainicial = data
                        try:
                            data_dia = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.ID, "exlidInput_drStartDay_"))
                            )

                            data_mês = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.ID, "exlidInput_drStartMonth_"))
                            )

                            data_ano = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, "//select[@id='exlidInput_drStartMonth_']/../input[@placeholder='Ano']"))
                            )

                            Select(data_dia).select_by_value(
                                str(datasplit[0]).zfill(2))
                            Select(data_mês).select_by_value(
                                str(datasplit[1]).zfill(2))
                            data_ano.clear()
                            data_ano.send_keys(str(datasplit[2]))

                        except:
                            print("Erro ao adicionar data inicial, tente novamente!")
                        else:
                            print("Data inicial inserida com sucesso!")
                            print(self.datainicial)
                            break
                    else:
                        print("Data em formato incorreto!")
                except:
                    print("Data em formato incorreto!")
            else:
                print("Data em formato incorreto!")
        self.açãoPré()

    def addDataFinal(self):
        while True:
            data = input("Digite a data (dd/mm/aaaa): ")
            os.system('cls' if os.name == 'nt' else 'clear')
            datasplit = data.split("/")

            if len(datasplit) == 3:
                try:
                    datasplit[0] = int(datasplit[0])
                    datasplit[1] = int(datasplit[1])
                    datasplit[2] = int(datasplit[2])

                    if datasplit[0] > 0 and datasplit[0] <= 31 and datasplit[1] > 0 and datasplit[1] <= 12:
                        self.datafinal = data
                        try:
                            data_dia = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.ID, "exlidInput_drEndDay_"))
                            )

                            data_mês = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.ID, "exlidInput_drEndMonth_"))
                            )

                            data_ano = WebDriverWait(self.driver, 10).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, "//select[@id='exlidInput_drEndMonth_']/../input[@placeholder='Ano']"))
                            )

                            Select(data_dia).select_by_value(
                                str(datasplit[0]).zfill(2))
                            Select(data_mês).select_by_value(
                                str(datasplit[1]).zfill(2))
                            data_ano.clear()
                            data_ano.send_keys(str(datasplit[2]))
                        except:
                            print("Erro ao adicionar data final, tente novamente!")
                        else:
                            print("Data final inserida com sucesso!")
                            print(self.datafinal)
                            break
                    else:
                        print("Data em formato incorreto!")
                except:
                    print("Data em formato incorreto!")
            else:
                print("Data em formato incorreto!")
        self.açãoPré()

    def buscar(self):
        print("Iniciando busca...")
        try:
            buscar_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "goButton"))
            )

            buscar_button.click()
        finally:
            print("Busca iniciada!")
            self.açãoPós()

    def açãoPós(self):
        try:
            resultadoquantidade = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='resultsNumbersTile']//h1//em"))
            )
            self.resultadosquantidade = resultadoquantidade.get_attribute(
                "innerHTML").strip()
        except:
            self.resultadosquantidade = "Erro ao identificar total de resultados"
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Busca efetuada com sucesso!")
        print("Resultados encontrados: "+self.resultadosquantidade)
        print("\n")
        print("_____________________________")
        print("Opções:")
        print("1 - "+("Não mostrar" if self.revisãoporpares else "Mostrar") +
              " somente periódicos revisados por pares.")
        print("2 - Incluir tipo de recurso.")
        print("3 - Excluir tipo de recurso.")
        print("4 - Incluir tópico.")
        print("5 - Excluir tópico.")
        print("6 - Remover filtro.")
        print("7 - Salvar resultado.")
        print("8 - Fechar programa.")
        print("_____________________________")
        print("\n")
        ações = {
            1: self.mudarRevisãoPorPares,
            2: self.buscar,
            3: self.buscar,
            4: self.buscar,
            5: self.buscar,
            6: self.buscar,
            7: self.save,
            8: exit,
        }
        while True:
            try:
                ação = int(input("Digite a opção desejada: "))
                ação = ações[ação]
            except:
                print("Opção inválida!")
                print("\n")
                continue
            else:
                break

        print("\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        ação()

    def save(self):
        print("Iniciando extração de dados!")

        morepages = True
        relevancia = 1
        lista_resultados = []
        lista_referencias = []
        lista_autores = []
        lista_autores_instituicao = []
        while (morepages):
            tabela = WebDriverWait(self.driver, 10).until(
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

            referencias_buttons = tabela.find_elements(By.CSS_SELECTOR, "[md-svg-icon='primo-ui:citing']")

            i = 0;

            for button in referencias_buttons:
                #try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "#searchElementsWrapper"))
                )
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, ".list-item-primary-content"))
                )
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_all_elements_located(
                        (By.CSS_SELECTOR, f"[md-svg-icon=\'primo-ui:citing\']"))
                )
                time.sleep(4)
                try:
                    self.driver.execute_script(f'document.querySelectorAll("[md-svg-icon=\'primo-ui:citing\']")[{i}].click()')
                    i+=1
                    #button.click()\\
                    
                    referencias_button_close = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".back-button"))
                    )
                    
                    referencias = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".result-item-details .item-title"))
                    )
                    
                    referencias = self.driver.find_elements(By.CSS_SELECTOR, ".result-item-details .item-title")
                    for referencia in referencias:
                        lista_referencias.append([título, referencia.get_attribute("innerText")])

                    time.sleep(2)
                    self.driver.execute_script(f'window.history.go(-1)')
                    
                except:
                    time.sleep(2)
                    self.driver.execute_script(f'window.history.go(-1)')
                    #referencias = []
                    
                finally:
                    #referencias_button_close.click()
                    #self.driver.execute_script(f'document.querySelector(".back-button").click()')
                    continue
                    
                

            try:
                proximo = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.counter-next:not(.ng-hide)')))
                proximo.click()
                morepages = True
            except:
                morepages = False

        for autor in lista_autores:
            try:
                url_orcid = f'https://orcid.org/orcid-search/search?searchQuery={autor[1]}'

                self.driver.get(url_orcid)
            
            
                autor_instituicao = WebDriverWait(self.driver, 10).until(
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
                    

        self.df = pd.DataFrame(lista_resultados, columns=[
            "Relevância", "Título", "Link", "Autor", "Publicação", "Descrição"])

        self.df_referencias = pd.DataFrame(lista_referencias, columns=[
            "Título", "Referência"])

        self.df_autores = pd.DataFrame(lista_autores_instituicao, columns=[
            "Título", "Autor", "Instituição", "País"])

        #orcid = Orcid().pesquisar()

        #self.df = orcid.busca(self.df)

        self.açãoSalvamento()

        '''try:
            resultadosquantidade = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='mainResults']/prm-search-result-tool-bar/div/md-toolbar/div[2]/span[2]"))
            )

            resultadosquantidade = resultadosquantidade.get_attribute(
                "innerHTML")

            resultadosquantidade = re.sub('[^0-9]', '', resultadosquantidade)

            self.resultadosquantidade = int(resultadosquantidade)
        except:
            self.resultadosquantidade = None
            print("Erro ao encontrar resultados! Tente novamente mais tarde!")
        else:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("Resultados encontrados: "+str(self.resultadosquantidade))

            pages = math.floor(self.resultadosquantidade/10)
            print("Número de páginas: "+str(pages))

            lista_resultados = []

            for page in range(pages):
                print("Página: "+str(page)+" de "+str(pages) )
                tabela = WebDriverWait(self.driver, 10).until(
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
                    proximo = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//a[@ng-click="$ctrl.getNextPage($event)"]')))
                    proximo.click()
                except:
                    pass

            self.df = pd.DataFrame(lista_resultados, columns=[
                "Relevância", "Título", "Link", "Autor", "Publicação", "Descrição"])

            orcid = Orcid().pesquisar()

            self.df = orcid.busca(self.df)

            self.driver.quit()

            self.açãoSalvamento()'''

    def açãoSalvamento(self):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Dados salvos com sucesso!")
        print("\n")
        print("_____________________________")
        print("Opções:")
        print("1 - Exportar para Excel.")
        print("2 - Exportar para JSON.")
        print("3 - Exportar para CSV.")
        print("4 - Mostrar resultado.")
        print("5 - Fechar programa.")
        print("_____________________________")
        print("\n")
        ações = {
            1: self.export_to_Excel,
            2: self.export_to_JSON,
            3: self.export_to_CSV,
            4: self.print_DF,
            5: self.exit
        }
        while True:
            try:
                ação = int(input("Digite a opção desejada: "))
                ação = ações[ação]
            except:
                print("Opção inválida!")
                print("\n")
                continue
            else:
                break

        print("\n")
        #os.system('cls' if os.name == 'nt' else 'clear')
        ação()

    def export_to_Excel(self):
        df_json = self.df.to_excel(f"./Resultados/busca.xlsx")
        df_json_referencias = self.df.to_excel(f"./Resultados/referencias.xlsx")
        df_json_autores = self.df.to_excel(f"./Resultados/autores.xlsx")
        self.açãoSalvamento()
        
    def export_to_JSON(self):
        df_json = self.df.to_json(orient='records', force_ascii=False)
        file = codecs.open("./Resultados/busca.json", "w", "utf-8")
        file.write(df_json)
        file.close()

        df_json_referencias = self.df_referencias.to_json(orient='records', force_ascii=False)
        file = codecs.open("./Resultados/referencias.json", "w", "utf-8")
        file.write(df_json_referencias)
        file.close()

        df_json_autores = self.df_autores.to_json(orient='records', force_ascii=False)
        file = codecs.open("./Resultados/autores.json", "w", "utf-8")
        file.write(df_json_autores)
        file.close()

        self.açãoSalvamento()

    def export_to_CSV(self):
        df_json = self.df.to_csv(f"./Resultados/busca.csv")
        df_json_referencias = self.df_referencias.to_csv(f"./Resultados/referencias.csv")
        df_json_autores = self.df_autores.to_csv(f"./Resultados/autores.csv")

        self.açãoSalvamento()

    def print_DF(self):
        print(self.df)
        self.açãoSalvamento()

    def exit(self):
        self.driver.quit()
        os.system('cls' if os.name == 'nt' else 'clear')


        # link de teste.
        # https://capes-primo.ezl.periodicos.capes.gov.br/primo-explore/search?query=any,contains,teste&tab=default_tab&search_scope=default_scope&vid=CAPES_V3&facet=rtype,include,books&facet=tlevel,include,peer_reviewed&lang=pt_BR&offset=0
