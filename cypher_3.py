from turtle import numinput
import os

#Globale variabler
alfabet = "abcdefghijklmnopqrstuvwxyzæøå" 

#funksjon som skal lage cæsar-kode
def encode(bokstav, nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos + nøkkel)
    if ny_pos >= 29:
        ny_pos = ny_pos - 29
    return alfabet[ny_pos]

#funksjon for å oversette cæsar-koden
def decode(bokstav,nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos - nøkkel)
    if ny_pos < 0:
        ny_pos = ny_pos + 29
    return alfabet[ny_pos]

#Lage krypterte meldinger
def encrypt():
    output = ""
    nøkkel = int(input("What key(1-9) shall I use for this message? \n"))
    melding_1 = input("Write the message you want me to encrypt.\n")
    for c in melding_1:
        if c in alfabet:
            output += encode(c, nøkkel)
        else:
            output += c
    print("\nEncryption completed!\nYour encrypted message using key",nøkkel,"is:", output, "\n\n")
    dostuff()
    return output
    
    
#oversette krypterte meldinger
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
    dostuff()
    os.system('cls||clear')
    return output
  
#Starte programmet, bruker "clear":
#Intro:
os.system('cls||clear')
def dostuff():
    print("Welcome to C-Cypher 1.0! \nI'm a simple program that can encrypt or decrypt messages using the \"Caesar cipher\" method!", "\n\nWhat do you want me to do next? \na: Encrypt a message.\nb: Decrypt a massage.\n")
    # Operasjoner bruker kan gjøre 
    kom = input("Please type a command:\n")
    if kom == "a":
        os.system('cls||clear')
        encrypt()
    elif kom == "b":
        os.system('cls||clear')
        decrypt()
dostuff()
