from random import *

def listaAlapok():
    #lista letrehozasa
    alapok=[]
    for i in range (10):
        alapok.append(randint(1,50))
    print(alapok)
    alapok.append('alma')
    alapok.append('leves')
    alapok.append('szilva')
    print(alapok)
    #lista kiírása szépen
    for item in alapok:
        print(item, end=" ")
    print()
    print(alapok[4]) #4-es indexu elem (sorban az otodik)
    print(len(alapok)) #lista elemszáma
    alapok.insert(4,"körte") #elem beszurasa az adott helyre      
    print(alapok.index('körte')) #elem indexe
    #print(alapok.index(55))
    alapok.remove('körte') # elem torlese
    alapok.pop() #utolso torlese
    del alapok[-1] #utolso torlese +1
    del alapok[1] #1-es index torlese
    #alapok.clear() #a lista elemeket torli
    #del alapok #a teljes listat torli
    alapok.reverse() # megforditja a sorrendet
    #alapok.sort() #novekvo sorrendbe teszi
    #alapok.reverse()
    print()
    print(alapok[5:]) #otos indextol a vegeig
    print(alapok[:4])
    print(alapok[-1])
    print(alapok[-2])
    print(alapok[-2:])
    print(alapok[3:5]) 
    alapok[6]='narancs'
    print(alapok[6])
    print()
    for item in alapok:
        print(item,end=" ")
    print()

def felatad1():

    elemszam=int(input("Add meg az elemek számát! :"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    paratlandb=0
    for item in szamok:
        if item%2==1:
            paratlandb+=1
    print("A páratlanok száma",paratlandb)



def feladat2():

    elemszam=int(input("Add meg az elemek számát! :"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    osszeg=0
    for item in szamok:
        if item%2==0:
            osszeg+item
    print("A párosok összege",osszeg)
    
def feladat4():

    elemszam=int(input("Add meg az elemek számát! :"))
    szamok=[]
    for i in range(elemszam):
        szamok.append(randint(1,50))
    print(szamok)
    for i in range(len(szamok)):
        if szamok[i]%2==0:
            print(i, "/t")







#listaAlapok()
#felatad1()
feladat2()







