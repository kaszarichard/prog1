#1.feladat:

n=('1 2 3 4 5 6 7 8 9 end')
oldalak=n.split(" ")
lista=[]

for i in  range (len(oldalak)):
    if oldalak[i]=="end":
        break
    else:
        lista.append(oldalak[i])

a=lista[0::3]
b=lista[1::3]
c=lista[2::3]
haromszogek_szama=int(len(lista)/3)

for i in range (haromszogek_szama):
    a[i],b[i],c[i]=int(a[i]),int(b[i]),int(c[i])
    if a[i]+b[i]>c[i] and a[i]+c[i]>b[i] and b[i]+c[i]>a[i]:
        print("szerkesztheto")

    else:
        print("nem szerkesztheto")

#2.feladat:

def haromszog_terulete(a,b,c,tipus):
    if tipus=="szerkesztheto":
        s=(a+b+c)//2
        t=(s*(s-a)*(s-b)*(s-c))**0.5
        return t


n = ('1 2 3 4 5 6 7 8 9 end')
oldalak = n.split(" ")
lista = []

for i in range(len(oldalak)):
    if oldalak[i] == "end":
        break
    else:
        lista.append(oldalak[i])

a = lista[0::3]
b = lista[1::3]
c = lista[2::3]
haromszogek_szama = int(len(lista) / 3)

for i in range(haromszogek_szama):
    a[i], b[i], c[i] = int(a[i]), int(b[i]), int(c[i])
    if a[i] + b[i] > c[i] and a[i] + c[i] > b[i] and b[i] + c[i] > a[i]:
        print("szerkesztheto, " +"terulet= " +str(haromszog_terulete(a[i], b[i], c[i], "szerkesztheto")))


    else:
        print("nem szerkesztheto")

#3.feladat:

def sum_mag(string):
    sum=0
    mag=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]

    for c in string:
        if c in mag:
            sum+=1
    return sum

szoveg="aefghjiok"
print(sum_mag(szoveg))

