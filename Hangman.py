"""
1- Pegar as palavras do arquivo.txt, usar .upper() para não dar erro com maiúsculo ou minusculo. Precisa usar o random nessa função.
2- Falar o tamanho da palavra, começar com uma print de um número mesmo.
3- Pedir para o usuário as letras (tem que estar dentro de um loop) (while vida < 6 ou acertar a palavra)
4- Gravar as letras digitadas, diferenciando entre letras da palavra e letras erradas. Precisa de um set vazio fora do loop para gravar
as letras erradas e outro set com as letras certas (isso tem como fazer assim: palavra = casa, digito = a, mostrar = _a_a.
5- Se (if) a letra estiver na palavra, mostrar, se não, mostrar em outro lugar, diminuindo uma vida do jogador (total 6 vidas)
6- Fazer o loop pro jogo rodar até o jogador acertar a palavra ou as vidas acabarem. (if)
7- printar "você ganhou" ou "você perdeu, a palavra era..."
"""

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


#import
import random
palavra = (random.choice(open("palavras.txt").read().split('\n')))

# Variables
letras_palavras = set(palavra)
letras_erradas = []
letras_certas = set()
letras_digitadas = set()


print(f"A palavra tem {len(palavra)} letras")

# Loop que termina com 6 erros ou palavra certa!
while len(letras_erradas) < 6 and len(letras_palavras) > 0:
    letra = input("Escolha uma letra: ").lower()  # guardar letra digitada temporariamente

    if letra in letras_digitadas:
        print("Você já digitou essa letra, tente outra!")
    else:
        letras_digitadas.add(letra)

        if letra in palavra:
            letras_certas.add(letra)  # Se acertou a letra, printa
            print("Acertou")

    #retirar a letra certa do set "letras_palavras" para quando o
    #jogador ganhar, existir a condição (len(letras_palavras) > 0
            if letra in letras_palavras:
                letras_palavras.remove(letra)

    # Quando a letra for errada, adiciona à lista[letras erradas] e faz os prints
        else:
            for letras in letra:
                letras_erradas.append(letra)
            print(board[len(letras_erradas)])
            print("Essa letra não existe na palavra.")
            print(f'Letras erradas: {letras_erradas}')

        if len(letras_erradas) == 6:
            print("Você perdeu!")
            break

        letras_palavra = [letter if letter in letras_certas else '_' for letter in palavra]
        print("Palavra:", ' '.join(letras_palavra))
        
        #Doing some test

# Doing a test