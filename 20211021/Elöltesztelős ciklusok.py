def feladat24():
    szam=float(input("Kérekegy számot! : "))
    while szam!= 0:
        szam=float(input("Másik számot kérek!: "))


#feladat24()

def feladat25():
    szam = float(input("Kérek egy pozitív számot! : "))
    
    while szam<=0:
        szam = float(input("Kérek egy másik számot! : "))


#feladat25()

def feladat26():
    szam = float(input("Kérek egy számot! : ")) 
    osszeg = szam
    while szam>10:         
         szam = float(input("kérek egy másik számot! : "))
         osszeg += szam
    print("A számok összege", osszeg)

feladat26()









