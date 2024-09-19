from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time



# Instalação do WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
# Acessa o site
navegador.get("https://rpachallengeocr.azurewebsites.net/")
time.sleep(3)


# Localiza o elemento da tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME ,"tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

dataframw_lista = []

linha = 1

for linhasAtual in linhas:
    print(linhasAtual.text)
    dataframw_lista.append(linhasAtual.text)

    linha = linha + 1

arquivoExcel = pd.ExcelWriter('dados.xlsx', engine='xlswriter')



