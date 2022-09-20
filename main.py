import asyncio
import numpy as np

sequencia = ['P', 'P', 'P', 'P', 'P', 'P', 'B', 'B', 'B', 'B']

class Padroes:
    def __init__(self , base , quebra , entrar, ganhou, perdeu):
        self.base = base
        self.quebra = quebra

    def montagem(self,base, quebra):
        self.entrar = [base , base]
        self.ganhou = [quebra, base, base]
        self.perdeu = [base ,base , base] or ['B',base ,base]

padrão2x1p = Padroes('P','V')


def padrao(live):
    if '0' < live <= '7':
        sequencia.append('V')
    elif live >= '8':
        sequencia.append('P')
    elif live == '0':
        sequencia.append('B')


def dados(add):
    while add <= 9:
        live = input("inserir numero: ")
        padrao(live)
        if add >= 9:
            sequencia.pop(0)
        else:
            add += 1

        print(sequencia)
        print(sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9])



# if [sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') == 4 and [sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') != 5:
#     print("ENTRAR!padrão 4x1")
#     if [sequencia[5] ,sequencia[6], sequencia[7], sequencia[8], sequencia[9]] == ['P' ,'P', 'P', 'P', 'V'] and [sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]] != ['P' ,'P', 'P', 'P', 'P' ,'P', 'P', 'V']:
#         print("GANHOU! padrão 4x1")
#
#     if ([sequencia[3], sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') == 7 or [sequencia[7], sequencia[8], sequencia[9]] == ['P' ,'P', 'B']) and [sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') != 8:
#         print("PARAR!padrão 4x1")
#
#     if [sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') == 5 and [sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8], sequencia[9]].count('P') != 6:
#         print("DOBRAR APOSTA!padrão 4x1")
#         if ([sequencia[3], sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8],
#              sequencia[9]].count('P') == 7 or [sequencia[7], sequencia[8], sequencia[9]] == ['P', 'P', 'B']) and [
#             sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6], sequencia[7], sequencia[8],
#             sequencia[9]].count('P') != 8:
#             print("PARAR!padrão 4x1")
#
#
#     if sequencia[9] == 'B':
#         print("QUEBRA DE PADROES, AGUARDE PADRÃO!")


# def padroes_2x1(wp2,lp2):
#     global sequencia
#     if [sequencia[7], sequencia[8], sequencia[9]] == ['P' ,'P', 'V'] and [sequencia[6], sequencia[7], sequencia[8], sequencia[9]] !=  ['P' ,'P' ,'P', 'V']:
#         print("GANHOU! padrão 2x1")
#         wp2+=1
#     elif ([sequencia[7], sequencia[8], sequencia[9]].count('P') == 3  or [sequencia[7], sequencia[8], sequencia[9]] == ['P' ,'P', 'B']) and [sequencia[6], sequencia[7], sequencia[8], sequencia[9]] !=  ['P' ,'P' ,'P', 'P']:
#         print("PARAR padrão 2x1")
#         lp2+=1
#     elif [sequencia[8], sequencia[9]].count('P') == 2 and [sequencia[7], sequencia[8], sequencia[9]] != ['P' ,'P', 'P'] :
#         print("ENTRAR")
#
#
# def poseidon(wp3,lp3):
#     global sequencia
#     if [sequencia[0] ,sequencia[1] ,sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6] ,sequencia[7], sequencia[8], sequencia[9]] == ['P' ,'P' ,'P', 'P', 'P','P' ,'P', 'P', 'P', 'V']:
#         print("GANHOU!!! poseidon")
#         wp3+=1
#     elif [sequencia[1] ,sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6] ,sequencia[7], sequencia[8], sequencia[9]].count('P') == 9 and [sequencia[0], sequencia[1] ,sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6] ,sequencia[7], sequencia[8], sequencia[9]].count('P') != 10 :
#         print("ENTRADA POSEIDON 3X VALOR!")
#     elif [sequencia[0] ,sequencia[1] ,sequencia[2], sequencia[3], sequencia[4], sequencia[5], sequencia[6] ,sequencia[7], sequencia[8], sequencia[9]].count('P') == 10 and [list[0] ,list[1] ,list[2], list[3], list[4], list[5], list[6] ,list[7], list[8], list[9], list[10]] != 11:
#         print("PARARRR!!!")
#         lp3+=1


# dados(add)














# async def main():
#     await asyncio.gather(dados(add))


