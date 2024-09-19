from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Instalação do WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.totalacesso.com/")

navegador.find_element(By.XPATH, '//*[@id="header"]/div/div/div[2]/button[1]').click()
time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/form/mat-form-field[1]/div[1]').click()
time.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="userLogin"]').send_keys('renansantos140406@gmail.com')
time.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="password"]').click()
time.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys('Renan4022#')
time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="content"]/div[2]/form/button').click()
time.sleep(5)