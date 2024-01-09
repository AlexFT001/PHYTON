import random 
from palavras import words
import os
from time import sleep

def getPalavra(palavras):
    return random.choice(palavras)

def searchletter(guess, palavra):
    positions = []

    for index, letter in enumerate(palavra, start=0):
        if letter.upper() == guess.upper():
            positions.append(index)

    return positions

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 

        
palavra = getPalavra(words)
tentativa = []

for index, letter in enumerate(palavra, start=0):
        if letter.upper() == " ":
            tentativa.append(letter)
        else:
            tentativa.append("_")


while listToString(tentativa).replace(" ", "") != palavra.upper().replace(" ", ""):
    print(listToString(tentativa))
    print("Tell me your guess:")
    guess = input()
    if(len(guess) > 1):
        print("Isto é um jogo da forca vai brincar com outro!!")
    else:
        letter_positions = searchletter(guess, palavra)

        if len(letter_positions) > 0:
            for position in letter_positions:
                tentativa[position] = guess.upper()
        else:
            print("És um merdas,\nadvinha de uma vez.\nÉ fácil!!!")

os.system('cls')
print("\t\t\t\t\n\n\n\nBom Trabalho!!\n\n\n\n")
    



