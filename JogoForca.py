import requests
import os
import sys
from lxml import html  
from unidecode import unidecode

mensagem_parabens = """
  ___                  ___  
 (o o)                (o o) 
(  V  ) Parabéns !!! (  V  )
--m-m------------------m-m--
"""
mensagem_triste = """
  ^~^  ,                            
 ('Y') )   Fim de Jogo !!!                      
 /   \/  que pena você perdeu  __QQ 
(\|||/)                       (_)_">
                             /          
"""

def remover_acentos(texto):
    return unidecode(texto)

def limpar_tela():
    os.system('cls')

escolha = "s"

while escolha != "n":
    
    limpar_tela()
    
    def carrega_palavra_secreta():
        url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
        resposta = requests.get(url)
        elemento = html.fromstring(resposta.content)
        palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
        palavra_secreta = palavra_secreta[0].strip()
        return palavra_secreta

    palavra_secreta = remover_acentos(carrega_palavra_secreta())
    tentativas = 5
    limite = 0

    estado_atual = ["_"] * len(palavra_secreta)
    letras_escolhidas = []

    print()
    print("Bem vindo ao jogo da forca !!!")
    print("Seu objetivo e tentar encontrar a palavra secreta")
    print("tente advinhar 1 letra por vez, Você tem ", tentativas ," tentativas")
    print()
    print(estado_atual)
        
    while tentativas > 0 and "".join(estado_atual) != palavra_secreta:
        print()
        letra = input("Digite uma letra: ")

        while letra in letras_escolhidas:
            print("Esta letra já foi utilizada tente novamente")
            letra = input("Digite uma letra: ")
            print()

        if letra in palavra_secreta:
            print("Letra Correta !!")

            for i in range(len(estado_atual)):
                if letra == palavra_secreta[i]:
                    estado_atual[i] = letra
            
            letras_escolhidas.append(letra)
            print(estado_atual)
            print()

        else:
            tentativas -= 1
            letras_escolhidas.append(letra)
            print("você errou !!")
            print("Ainda restam ", tentativas, "tentativas")
            print("Você já usou estas letras: ", letras_escolhidas)
            print()

    if tentativas == limite:
        print(mensagem_triste)
        print("Fim de Jogo !!!") 
        print("A palavra secreta era:", palavra_secreta)   
        print()
        escolha = input("Deseja Jogar Novamente S/N ?")
    else:
        print(mensagem_parabens)
        print("você encontrou corretamente todas as letras")
        print("A palavra secreta era:", palavra_secreta)
        print()
        escolha = input("Deseja Jogar Novamente S/N ?")
    
sys.exit()   

