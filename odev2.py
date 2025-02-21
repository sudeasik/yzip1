faiz = 1.59
vade = "36"
krediAdi = "ihtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12) #tip dönüşümü, str -> int
faiz = str(faiz)
print(type(faiz))

vade = 36 #input("lütfen istediğiniz vade sayısını giriniz:")  #kullanıcıdan değer alma
print(type(vade))
print(int(vade) + 12)

#string interpolation
#Seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade) )


isim = "Halit"
metin = "Merhaba {name}".format(name="Samet")
print(metin)

#f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)


#listeler
#döngüler
dizi = ["İhtiyaç Kredisi", 10, 5.3]  #python'da liste elemanları farklı tiplerde olabılır.
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler)
print(krediler[0])

#print(krediler[5])  #indexerror -> out of range
print(len(krediler))  #listenin kaç elemanlı oldugunu soyler


krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)   #verilen indexteki elemanı siler. -1.index son imdeks demek
print(krediler)

krediler.remove("Taşıt Kredisi")  #index bazlı değil değer bazlı çalışır
print(krediler)



krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)



#döngüler
#for
# i=0 i<10


for i in range(10):
    print("xx")
    print(i)

print("******************")

for i in range(5,11):
    print(i)

print("*********************")

for i in range(0,51,10):
    print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)


print("***************")
for i in range(len(krediler)):
    print(krediler[i])


for i in range (len(krediler)):
    print(i)


#sonsuz döngü
i = 0
while i <10:
    print("x")
    i += 1 #i++
print("y")

print("*******************")

while True:
    print("X")
    break

print("*******************")

i = 0
while i < len(krediler):
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break


#fonksiyonlar

#print("Merhaba")
#print("Merhaba")
#print("Merhaba")
#print("Merhaba")

fiyat = 100
indirim = 20


#definition define
def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)
def sayHello(name):
    print(f"Merhaba {name}")
#calculate()
calculateWithParams(50,10)
calculateWithParams(100, 30)
sayHello("Halit")
sayHello("Arif")
sayHello("Mevlüt")


def calculateAndReturn(fiyat, indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)


def calculatePrice(price, discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price-discount


print("*****************")

fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(f"159.satır: {fonk1}")
print(f"160.satır: {fonk2+100}")
print("*****************")