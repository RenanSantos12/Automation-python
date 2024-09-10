import pyautogui as escolha_opcao

opcao = escolha_opcao.confirm('Clique no botão desejado', buttons=['Excel', 'Word', 'Notepad'])

if opcao == "Excel":
    print('Você escolheu abrir o execl')

    #precionando as teclas windows + R
    escolha_opcao.hotkey('win')

    #Espera dois segundos 
    escolha_opcao.sleep(2)

    #Digita excel
    escolha_opcao.typewrite('Excel')

     #Espera dois segundos 
    escolha_opcao.sleep(2)

    escolha_opcao.press('enter')

    #Espera cinco segundos 
    escolha_opcao.sleep(5)

    escolha_opcao.click(319, 103)

    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('Escolhi o Excel')

    

elif opcao == 'Word':
    print('Você escolheu abrir o Word')

    
    #precionando as teclas windows + R
    escolha_opcao.hotkey('win')

    #Espera dois segundos 
    escolha_opcao.sleep(2)

    #Digita excel
    escolha_opcao.typewrite('Word')

     #Espera dois segundos 
    escolha_opcao.sleep(2)

    escolha_opcao.press('enter')

     #Espera dois segundos 
    escolha_opcao.sleep(2)

    escolha_opcao.press('enter')
    
    escolha_opcao.typewrite('Escolhi abrir o Word')

    
else:
     
    #precionando as teclas windows + R
    escolha_opcao.hotkey('win')

    #Espera dois segundos 
    escolha_opcao.sleep(2)

    #Digita excel
    escolha_opcao.typewrite('Notepad')

     #Espera dois segundos 
    escolha_opcao.sleep(2)

    escolha_opcao.press('enter')

     #Espera dois segundos 
    escolha_opcao.sleep(2)

    escolha_opcao.press('enter')
    
    escolha_opcao.typewrite('Escolhi abrir o bloco de notas')

