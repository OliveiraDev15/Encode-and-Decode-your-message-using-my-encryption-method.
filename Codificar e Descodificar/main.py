from tools import *
from time import sleep


bem_vindo()

inicio = input("\n" + (" " * 4) +
               "O que deseja fazer? ").upper().strip()[0]

if inicio == 'C':
    texto1(frase())

elif inicio == 'D':
    texto2(frase2())

elif inicio == 'S':
    S()

else:
    error()

sair()
