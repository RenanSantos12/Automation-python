from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto("https://auth.totalacesso.com/login")
    time.sleep(3)

    pagina.locator('xpath=//*[@id="content"]/div[2]/form/mat-form-field[1]/div[1]/div/div[2]').click
    time.sleep(2)
    pagina.fill('xpath=//*[@id="content"]/div[2]/form/mat-form-field[1]/div[1]/div/div[2]', "renansantos140406@gmail.com")
    time.sleep(10)
    