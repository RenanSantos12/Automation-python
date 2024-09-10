from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 

Servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=Servico)

navegador.get("https://sociotorcedor.com.br/")
time.sleep(60)


navegador.find_element('xpath', '/html/body/app-root/div/fengstlayout-header/fengstlayout-header-v3/header/section/nav/a[1]').click()
navegador.find_element('xpath','//*[@id="mat-dialog-0"]/fengstauth-modal-auth-st/div/div/mat-dialog-content/div[3]/form/fengstui-input[1]/section/mat-form-field/div/div[1]').send_keys("renansantos140406@gmail.com")
navegador.find_element('xpath', '//*[@id="mat-dialog-0"]/fengstauth-modal-auth-st/div/div/mat-dialog-content/div[3]/form/fengstui-input[2]/section/mat-form-field/div/div[1]').send_keys('Renan4022#')
navegador.find_element('xpath', '//*[@id="mat-dialog-0"]/fengstauth-modal-auth-st/div/div/mat-dialog-content/div[3]/form/fengstui-button/button').click()