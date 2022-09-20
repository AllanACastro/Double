import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from collections.abc import Mapping
import time
import re
import datetime
import numpy as np



ganhou = 0
perdeu = 0
entrou = 0

contagem_p4P = {'ganhou': 0, 'perdeu': 0, 'entrou' : 0}
contagem_p4V = {'ganhou': 0, 'perdeu': 0, 'entrou' : 0}
contagem_p3P = {'ganhou': 0, 'perdeu': 0, 'entrou': 0}
contagem_p3V = {'ganhou': 0, 'perdeu': 0, 'entrou': 0}
contagem_p2P = {'ganhou': 0, 'perdeu': 0, 'entrou': 0}
contagem_p2V = {'ganhou': 0, 'perdeu': 0, 'entrou': 0}


# contagem_tiro = {'ganhou': 0, 'perdeu': 0}

def padrao(live):
   
    if 0 < live <= 7:
        live = 'V'
    elif live >= 8:
        live = 'P'
    elif live == 0:
        live = 'B'
        
    return live

entrou2x1 = False
entrou3x1 = False
entrou4x1 = False

def padroes_preto():
    global sequencia
    global entrou4x1

    if not entrou4x1 and sequencia[:4].count('P') == 4 and sequencia[:5].count('P') != 5:
        print("ENTRAR!padrão  p 4x1\n")
        entrou4x1 = True
        return 'entrou'
                                                             

    elif entrou4x1 and sequencia[:5] == [ 'V','P' ,'P', 'P', 'P'] and sequencia[:6] != [ 'V','P', 'P', 'P', 'P' ,'P']:
        print("GANHOU! padrão 4x1p\n")
        entrou4x1 = False
        return 'ganhou'

    elif entrou4x1 and (sequencia[:5].count('P') == 5 or sequencia[:5] == ['B','P' ,'P' ,'P' ,'P']) and sequencia[:6].count('P') != 6:
        print("PARAR!padrão 4x1p\n")
        entrou4x1 = False
        return 'perdeu'

        

#     elif entrou4x1 [sequencia[0], sequencia[1], sequencia[2], sequencia[3], sequencia[4]].count('P') == 5 and [sequencia[0], sequencia[1], sequencia[2], sequencia[3], sequencia[4], sequencia[5]].count('P') != 6:
#         print("DOBRAR APOSTA!padrão p 4x1\n")
#         entrou4x1 = True
#         return 'dobra'



def padroes_vermelho():
    global sequencia
    global entrou4x1

    if not entrou4x1 and sequencia[:4].count('V') == 4 and sequencia[:5].count('V') != 5:
        print("ENTRAR!padrão  p 4x1\n")
        entrou4x1 = True
        return 'entrou'                                                     

    elif entrou4x1 and sequencia[:5] == [ 'P','V' ,'V', 'V', 'V'] and sequencia[:6] != [ 'P','V', 'V', 'V', 'V' ,'V']:
        print("GANHOU! padrão 4x1p\n")
        entrou4x1 = False
        return 'ganhou'

    
    elif entrou4x1 and (sequencia[:5].count('V') == 5 or sequencia[:5] == ['B','V' ,'V' ,'V' ,'V']) and sequencia[:6].count('V') != 6:
        print("PARAR!padrão 4x1p\n")
        entrou4x1 = False
        return 'perdeu'

        

#     elif entrou4x1 [sequencia[:5].count('P') == 5 and [sequencia[:6].count('P') != 6:
#         print("DOBRAR APOSTA!padrão p 4x1\n")
#         entrou4x1 = True
#         return 'dobra'
#
#
#
#     elif  [sequencia[0], sequencia[1], sequencia[2]] == ['B', 'V' ,'V']:
#         print("QUEBRA DE PADROES, AGUARDE PADRÃO!\n")

        
def padroes_3x1_preto():
    global sequencia
    global entrou3x1

    minilista = sequencia[:5]
    if not entrou3x1 and minilista[:3].count('P') == 3 and minilista[:4].count('P') != 4:
        print("ENTRAR!padrão  p 3x1\n")
        entrou2x1 = True
        return 'entrou'

    elif entrou3x1 and minilista[:4] == ['V','P' ,'P','P'] and minilista != [ 'V', 'P', 'P', 'P','P']:
        print("GANHOU! padrão 3x1 p\n")
        entrou3x1 = False
        return 'ganhou'
        
    elif entrou3x1  and minilista[:4].count('P') == 4 or minilista[:4] == ['B','P' ,'P','P']:
        print("PARAR!padrão 3x1 p\n")
        entrou3x1 = False
        return 'perdeu'
        
#     elif entrou and minilista[:3].count('P') == 3 and minilista[:4].count('P') != 4:
#         print("DOBRAR APOSTA!padrão p 2x1\n")
#         entrou = True
#         return 'dobra'
        


        

        
def padroes_3x1_vermelho():
    global sequencia
    global entrou3x1
    
    minilista = sequencia[:5]

    if not entrou and minilista[:3].count('V') == 3 and minilista[:4].count('V') != 4:
        print("ENTRAR!padrão  v 3x1\n")
        entrou3x1 = True
        return 'entrou'

    elif entrou and minilista[:4] == ['P','V' ,'V','V'] and minilista != [ 'P', 'V', 'V', 'V','V']:
        print("GANHOU! padrão 3x1 v\n")
        entrou3x1 = False
        return 'ganhou'
        
    elif entrou and minilista[:4].count('V') == 4 or minilista[:4] == ['B','V' ,'V','V']:
        print("PARAR!padrão 3x1 v\n")
        entrou3x1 = False
        return 'perdeu'                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
def padroes_2x1_preto():
    global sequencia
    global entrou2x1

    minilista = sequencia[:5]
    if not entrou2x1 and minilista[:2].count('P') == 2 and minilista[:3].count('P') != 3:
        print("ENTRAR!padrão  p 2x1\n")
        entrou2x1 = True
        return 'entrou'

    elif entrou2x1 and minilista[:3] == ['V','P' ,'P'] and minilista != [ 'V', 'P', 'P', 'P']:
        print("GANHOU! padrão 2x1 p\n")
        entrou2x1 = False
        return 'ganhou'
        
    elif entrou2x1  and (minilista[:3].count('P') == 3 or minilista[:3] == ['B','P' ,'P']):
        print("PARAR!padrão 2x1 p\n")
        entrou2x1 = False
        return 'perdeu'
        
#     elif entrou and minilista[:3].count('P') == 3 and minilista[:4].count('P') != 4:
#         print("DOBRAR APOSTA!padrão p 2x1\n")
#         entrou = True
#         return 'dobra'
        


        

        
def padroes_2x1_vermelho():
    global sequencia
    global entrou2x1
    
    minilista = sequencia[:5]

    if not entrou and (minilista[:2].count('V') == 2 and minilista[:3].count('V') != 3):
        print("ENTRAR!padrão  v 2x1\n")
        entrou2x1 = True
        return 'entrou'

    elif entrou and (minilista[:3] == ['P','V' ,'V'] and minilista != [ 'P', 'V', 'V', 'V']):
        print("GANHOU! padrão 2x1 v\n")
        entrou2x1 = False
        return 'ganhou'
        
    elif entrou and (minilista[:3].count('V') == 3 or minilista[:3] == ['B','V' ,'V']):
        print("PARAR!padrão 2x1 v\n")
        entrou2x1 = False
        return 'perdeu'
        

                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
                                                                                                       
url = "https://blaze.com/pt/games/double"

option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'C:\Users\forda\Desktop\projetin\geckodriver.exe')

driver.get(url)
# driver.implicitly_wait(10)  # in seconds
# time.sleep(10)

element = driver.find_element_by_xpath(f'.//div[@class="entries main"]')
odd = input("precione enter para começar(espere o contador estar em 14s)\n")

sequencia_anterior = []
# sequencia_num_anterior = []
while 1:
    global sequencia
    
    tempo = datetime.datetime.now().strftime('%H:%M')
    
    if tempo in ['22:00']:
        print("parou")
        
        time.sleep(7200)
        
    else:
        
    #element        = driver.find_element_by_xpath(f'.//div[@class="entries main"]//div[@class="number"]').click()


    # botaopreto    = driver.find_element_by_xpath(f'.//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[3]').click()
    # botaovermelho = driver.find_element_by_xpath(f'.//*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[1]').click()
    # botao2x       = driver.find_element_by_xpath(f'.//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/button[2]').click()
    # botao1x       = driver.find_element_by_xpath(f'.//*[@id="roulette-controller"]/div[1]/div[2]/div[1]/button[1]').click()


    # xpath botão preto        = //*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[3]
    # xpath botão vermelho     = //*[@id="roulette-controller"]/div[1]/div[2]/div[2]/div/div[1]
    # xpath botão 2x           = //*[@id="roulette-controller"]/div[1]/div[2]/div[1]/button[2]
    # xpath botão 1/2          = //*[@id="roulette-controller"]/div[1]/div[2]/div[1]/button[1]
    # xpath botão valor aposta = //*[@id="roulette-controller"]/div[1]/div[2]/div[1]/div

        element = driver.find_elements_by_class_name('sm-box')[:10]
        sequencia=[]
        lista_num =[]
        
        for tile in element:

        #         print(tile)

            html_content = tile.get_attribute('innerHTML')
            number = re.findall(r'(?i)<div.*?>([^<]+)</div.*?>', html_content)
            
            if len(number) > 0:
                lista_num.append(int(number[0]))

            elif len(number) == 0:
                lista_num.append(0)
            
            if len(number) > 0:
                sequencia.append(int(number[0]))

            elif len(number) == 0:
                sequencia.append(0)

        
        sequencia = [padrao(num) for num in sequencia]
        
#         if lista_num != sequencia_num_anterior:
#             sequencia_num_anterior = lista_num

            
        if sequencia != sequencia_anterior:

            for key in [padroes_2x1_preto()]:
                if key:
                    contagem_p2P[key] += 1
                    
            for key in [padroes_2x1_vermelho()]:
                if key:
                    contagem_p2V[key] += 1

            for key in [padroes_3x1_preto()]:
                if key:
                    contagem_p3P[key] += 1
                    
            for key in [padroes_3x1_vermelho()]:
                if key:
                    contagem_p3V[key] += 1   
                    
            for key in [padroes_preto()]:
                if key:
                    contagem_p4P[key] += 1
                    
            for key in [padroes_vermelho()]:
                if key:
                    contagem_p4V[key] += 1

                    
            print('lista do momento!')
            print(f'{sequencia}')
#             print(f'numeros:{lista_num}\n\n')
#             print(f'Tiro certo          = {contagem_tiro}')
            print(f'\n Padrão 2X1 PRETO    = {contagem_p2P}')
            print(f' Padrão 2X1 VERMELHO = {contagem_p2V}')
            print(f'\n Padrão 3x1 PRETO    = {contagem_p3P}')
            print(f' Padrão 3x1 VERMELHO = {contagem_p3V}')                                                                                 
            print(f'\n Padrão 4x1 PRETO    = {contagem_p4P}')
            print(f' Padrão 4x1 VERMELHO = {contagem_p4V}')
            print('________________________________________________________\n\n')
            
            sequencia_anterior = sequencia
            
            

        time.sleep(4)




