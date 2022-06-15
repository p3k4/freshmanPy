import datetime

#print('Hei på deg') #skriver ut en tekst-streng
#print(2+2)          #skriver ut utregning av 2+2
#print('6+6+6')      #skriver ut tekst-streng

# del 1 - Gjøre selv
#navn = "jeg"
#print("Hei, ", navn.capitalize(), "er en datamaskin.", navn.capitalize(), "er derfor kjempeflink i matematikk. Skal", navn, "vise deg?")
#Del 2 - Variabler

# del 2 - Variabler

#variabel = 4
#per = 'en gutt'
#frida = 'ei jente'
#et_tall = 3
#enda_et_tall = variabel + et_tall

#print(frida)
#print(frida)
#print(per)
#print(variabel - et_tall)
#print(enda_et_tall)

#iår = datetime.datetime.now().year #henter året vi er i
#p_født = 1991
#tekst = 'Jeg regnet ut at du er: '
#alder = iår - p_født
#print(tekst, alder, 'år')

#Del 3 - innputt
#navn = input('Hei! Hvem er du?\n')
#print('Hyggelig å møte deg,', navn,'\n')
#alder = int(input('Hvor gammel er du?\n'))
#neste_år = (alder + 1)
#print('Ja vel, til neste år blir du:', neste_år)

#Gjøre selv:
#f_år = int(input("Hvilket år er du født? \n"))
#alder = (datetime.datetime.now().year - f_år)
#print('Du er:', alder, 'år.')

#Del-4, if-setningen
#En if-setning er en måte for å bestemme hva datamaskinen skal gjøre ved å sjekke om noe er sant(if* betyr "hvis" på engenlsk). 
# Dersom if-setningen ikke er sann kan vi be datamasknenn gjøre noe annet, og vi bruker da "else" som er engelsk for "ellers".

#if dette_er_sant:
#    gjør_dette()
#elif noe_annet_er_sant:
#    gjør_noe_annet()
#else:
#    ingen_av_if_setningene_er_sann()
#
#prøv ut selv
#tekst = 'Heisann'
#if tekst == 'Hei':
#    print(tekst == 'Hei')
#elif tekst == 'Hoho':
#    print(tekst == 'Hoho')
#elif 'Hei' in tekst:
#    print('"Hei" er inni teksten!')
#else:
#    print('Teksten er ikke Hei, Hoho, og "Hei" er ikke inni teksten.')

# Gjøre selv:
alder = int(input('Hvilket år er du født?\n'))
alder_2 = (datetime.datetime.now().year - alder)
print(alder_2)
tekst_2 = input("Stemmer det at du er så gammel?\n")
if tekst_2 == 'Ja':
    print(tekst_2, 'Der ser du, jeg er kjemeflink i matematikk!\n')
elif tekst_2 == 'Nei' or tekst_2 == 'nei': 
    print('Brr-klikk-klakk.. \nEtter nøye omregning er du faktisk', alder_2 - 1,'!')
else:
    print("Error..")
    