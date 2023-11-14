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

# Função importada da biblioteca unidecode para remover as acentuações da palavra secreta
def remover_acentos(texto):
    return unidecode(texto)

# Função importada da biblioteca OS para limpar a interface de linha de comando
def limpar_tela():
    os.system('cls')

escolha = "s"

while escolha != "n":
    
    limpar_tela()
    
    # Função que conecta a uma página que gera palavras aleatoriamentee captura essa palavra para ser a palavra secreta
    def carrega_palavra_secreta():
        url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
        resposta = requests.get(url)
        elemento = html.fromstring(resposta.content)
        palavra_secreta = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
        palavra_secreta = palavra_secreta[0].strip()
        return palavra_secreta

    #Limpando os acentos da palavra importada
    palavra_secreta = remover_acentos(carrega_palavra_secreta())

    tentativas = 5
    limite = 0

    #O estado atual mostra varios caracteres '_' para cada letra conforme o tamanho da palavra secreta
    estado_atual = ["_"] * len(palavra_secreta)

    #Array para armazenar cada palavra que for escolhida pelo usuário
    letras_escolhidas = []

    print()
    print("Bem vindo ao jogo da forca !!!")
    print("Seu objetivo e tentar encontrar a palavra secreta")
    print("tente advinhar 1 letra por vez, Você tem ", tentativas ," tentativas")
    print()
    print(estado_atual)

    #Enquanto tentativas estiver maior que 0 e Estado atual estiver diferente da palavra secreta o loop e repetido
    while tentativas > 0 and "".join(estado_atual) != palavra_secreta:
        print()
        letra = input("Digite uma letra: ")

        #Loop de segurança para evitar que usuário selecione mais de uma letra ou deixe a seleção vazia
        while len(letra) > 1 or (letra == " ") or (letra == ""):
            print()
            print("Não e permitido deixar vazio ou digitar mais de uma letra por vez")
            letra = input("Digite uma letra: ")

        #Se a letra selecionada, estiver presente no Array letras_escolhidas, o loop se repete até escolher uma letra diferente
        while letra in letras_escolhidas:
            print("Esta letra já foi utilizada tente novamente")
            print()
            letra = input("Digite uma letra: ")

        #Se a letra estiver presente na palavra secreta, ela sera substituida no Array estado_atual
        if letra in palavra_secreta:
            print()
            print("Letra Correta !!")

            for i in range(len(estado_atual)):
                if letra == palavra_secreta[i]:
                    estado_atual[i] = letra
            
            letras_escolhidas.append(letra)
            print(estado_atual)
            print()
            print("Você já usou estas letras: ", letras_escolhidas)

        else:
            tentativas -= 1
            letras_escolhidas.append(letra)
            print()
            print("você errou !!")
            print("Ainda restam ", tentativas, "tentativas")
            print("Você já usou estas letras: ", letras_escolhidas)
            print()
    
    #Se as tentativas chegar a 0 o jogo e finalizado
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

#Caso o usuário selecione a opção N ao finalizar uma jogada, a função sys.exit() fechara o terminal    
sys.exit()   

