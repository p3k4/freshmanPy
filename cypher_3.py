from turtle import numinput
import os
#Globale variabler
alfabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ "
l = len(alfabet) 

#funksjon som skal lage cæsar-kode
def encode(bokstav, nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos + nøkkel) % l
    return alfabet[ny_pos]

#funksjon for å oversette fra cæsar-kode
def decode(bokstav,nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos - nøkkel) % l
    return alfabet[ny_pos]

#Lage krypterte meldinger
def encrypt():
    output = ""
    nøkkel = int(input("What key(#) shall I use for this message? \n"))
    melding_1 = input("Write the message you want me to encrypt.\n")
    for c in melding_1:
        if c in alfabet:
            output += encode(c, nøkkel)
        else:
            output += c
    print("\nEncryption completed!\nYour encrypted message using key",nøkkel,"is:", output, "\n")
    dostuff() #sender bruker tilbake til "start"
    return output
    
#Åpne krypterte meldinger
def decrypt():
    hemmelig_melding = input("What is the message you want me to decrypt?\n")
    nøkkel = int(input("What key shall I use to decrypt the message?\n"))
    output = ""
    for c in hemmelig_melding:
        if c in alfabet:
            output += decode(c,nøkkel)
        else:
            output += c
    print("\nDecryption completed!\nYour encrypted message using key",nøkkel,"is:", output, "\n\n")
    dostuff() #sender bruker tilbake til "start"
    os.system('cls||clear')
    return output
  
#Starte programmet
os.system('cls||clear')
def dostuff():
    print("Welcome to C-Cypher 1.0! \nI'm a simple program that can encrypt or decrypt messages using the \"Caesar cipher\" method!", "\n\nWhat do you want me to do next? \na: Encrypt a message.\nb: Decrypt a massage.\n")
    # Operasjoner en bruker kan gjøre 
    kom = input("Please type a command:\n")
    # kommando a = bruker kan "lage" en melding som skal krypteres
    if kom == "a":
        os.system('cls||clear')
        encrypt()
    # kommando b =  bruker kan "åpne" en melding som allerede er kryptert    
    elif kom == "b":
        os.system('cls||clear')
        decrypt()
    else:
        os.system('cls||clear')
        dostuff()
dostuff()
