from turtle import numinput

#Globale variabler
alfabet = "abcdefghijklmnopqrstuvwxyzæøå" 

#funksjon som skal lage cæsar-kode
def encode(bokstav, nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos + nøkkel)
    
    if ny_pos >= 29:
        ny_pos = ny_pos - 29
    return alfabet[ny_pos]

#funksjon for å lese cæsar-koden
def decode(bokstav,nøkkel):
    pos = alfabet.find(bokstav)
    ny_pos = (pos - nøkkel)

    if ny_pos < 0:
        ny_pos = ny_pos + 29
    return alfabet[ny_pos]

##lage krypterte bokstaver gjøres slik:
#print(encode("a",3))

#Lage krypterte meldinger
output = ""
nøkkel = int(input("Hva er din nøkkel? \n"))
melding_1 = input("Skriv din melding.\n")
for c in melding_1:
        if c in alfabet:
            output += encode(c, nøkkel)
        else:
            output += c
print("Cæsar-kodet: ", output, "\n")

#lagrer melding_1 irresolute 
melding_2 = output

#Tømmer "output" variablen.
output = ""

#oversette melding_1
for c in melding_2:
    if c in alfabet:
        output += decode(c,nøkkel)
    else:
        output += c
print("De-kodet Cæsar melding: ", output, "\n")