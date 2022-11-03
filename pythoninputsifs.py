#Da se napravi programa vo koja korisnikot ke vnese 2 broevi i da se proveri dali zbirot e pomal od 100
"""
broj1 = int (input ("Vnesete broj 1 "))
broj2 = int (input ("Vnesete broj 2 "))
zbir = broj1 + broj2

if zbir > 100:
    print ("Zbirot na broevite {} i {} iznesuva {} i e pogolem od 100  " .format (broj1, broj2, zbir))
else: 
    print ("Zbirot na broevite {} i {} iznesuva {} i e pomal od 100 " .format (broj1, broj2, zbir))



#Da se napravi programa vo koja korisnikot ke vnese godina na ragjanje, ke se presmeta kolku godini e i da se odredi dali e maloleten ili polnoleten

godinanaraganje = int (input ("Vnesete godina na raganje "))
godini = 2022 - godinanaraganje
godinidopolnoletstvo = 18 - godini
if godini >= 18:
    print ("Vie ste polnoleten/a  ")
else: 
    print ("Vie ste maloleten/a. Dojdete za {} godini koga ke imate 18 godini. Ubav den." .format (godinidopolnoletstvo))



#Da se napravi programa vo koja korisnikot ke vnese strani na dva pravoagolnici, da se presmeta plostinata i da se proveri koj pravoagolnik e pogolem


a= int (input ("Vnesete ja prvata strana na prviot pravoagolnik "))
b = int (input ("Vnesete ja vtorata strana na prviot pravoagolnik "))
c= int (input ("Vnesete ja prvata strana na vtoriot pravoagolnik "))
d = int (input ("Vnesete ja vtorata strana na vtoriot pravoagolnik "))

plostina1 = a * b
plostina2 = c*d

if plostina1 > plostina2:
    print ("Plostinata na prviot pravoagolnik e pogolema i iznesuva {}  " .format (plostina1))
else:
    print ("Plostinata na vtoriot pravoagolnik e pogolema i iznesuva {} " .format (plostina2))



#Da se napravi programa vo koja korisnikot ke vnese goleminite na aglite na triagolnici, 
# i da se proveri dali so tie golemini moze da se kreira triagolnik(zbirot treba da bide 180)

a = int (input ("Vnesete go prviot agol na triagolnikot "))
b = int (input ("Vnesete go vtoriot agol na triagolnikot "))
c = int (input ("Vnesete go tretiot agol na triagolnikot "))

zbir = a+b+c
nedostasuvaatstepeni = 180 - zbir

if zbir == 180:
    print ("So vnesenite agli {}, {}, {} moze da se kreira triagolnik" .format (a,b,c))
else:
    print ("So vnesenite agili ne moze da se kreira tiagolnik. Nedostasuvaat {} stepeni." .format(nedostasuvaatstepeni))
"""
#Da se napravi programa vo koja korisnikot ke vnese nekoe ime i da se proveri sekoga samoglaska 
# kolku pati se pojavuva vo ime i od kolku karakteri e sostaveno toa ime


string = input ("Vnesete go vaseto ime \n")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)