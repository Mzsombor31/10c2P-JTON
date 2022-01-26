from math import *
from random import *

def feladat1_5():

    a ="alma"
    print(type(a))

    b = "w"
    print(type(b))

    c = 12 
    print(type(c))

    d = 1.5
    print(type(d))

    e = True
    print(type(e))

def feladat6_9():
    szo = input("Kérek egy szót! :")
    print(szo)

    mondta = input("Kérek egy mondatot! :")
    print(mondta)

    karakter = input("Kérek egy karaktert! :")
    print(karakter)

    egeszszam = int(input("Kérek egy egész számot! :"))
    print(egeszszam, type(egeszszam))

def feladat10():
    vszam = float(input("Kérek egy valós számot! :"))
    print(vszam, type(vszam))
    print("Kétszer", vszam, "=", 2*vszam )
    print(vszam, "x pi =" , pi*vszam)
    print(vszam, "harmadik hatványa :" ,pow(vszam, 3))
    print(vszam, "négyzetgyöke: ", sqrt(vszam))
    print(vszam, "kerekített négyzetgyöke: ", round(sqrt(vszam), 2))

def feladat11_16():
    veletlen = randint(10, 50)
    print(veletlen)
    veletlen = random()
    print(veletlen)
    egesz = int(input("Kérek egy egész számot! :"))
    if egesz%2==0:
            print("A szám páros!")
    else:
        print("A szám páratlan!")
    if egesz>0:
        print("A szám pozitív")
    elif egesz<0:
        print("A szám negatív")
    else:
        print("A szám 0")
    if egesz>30:
        print("A szám több mint 30")
    else:
        print("A szám nem nagyobb mint 30")
    egyik = int(input("Kérek egy egesz szamot: "))
    masik = int(input("Kérek egy masik egyesz szamot: "))
    if egyik>masik:
        print("A nagyobb szam:", egyik)
    elif egyik<masik:
        print("A nagyobb szam:", masik)
    else: 
        print("A ket szam egyenlo!")
    if egyik<masik:
        print("A kisebb szam:", egyik)
    elif egyik>masik:
        print("A kisebb szam:", masik)
    else: 
        print("A ket szam egyenlo!")

#feladat1_5()
#feladat6_9()
#feladat10()
#feladat11_16()