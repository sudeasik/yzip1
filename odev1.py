print("Kodlamaio")
baslik = "Taşıt kredisi"
print(baslik)
#string = metinsel ifade
baslik="İhtiyaç Kredisi"
print(baslik)

#int, integer = tam sayı
vade = 36
ekVade = 6
vade2="36"

#vade + 2 = 38
#vade + 2 = 38

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean = true ya da false
yukselisteMi = True


 #matematiksel operatörler
 #+
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

#-
print(5-5)
print(vade - 12)
print(vade - ekVade)

#*
print(5*5)
print(vade*2)
print(vade * ekVade)

#/ , float değer döndürür
print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

#mod operatörü , kalan bulur
print(10%2)
print(vade % 3)


#mantıksal operatörler
print(1 == 1)
print (1 == 2)
print(1 > 3)
print(1!=2)

#or and
print(1>2 or 5>2)
print(1>2 and 5>2)


#karar yapıları
#if else

sayi1 = 10
sayi2 = 25
#sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition

#indent
if sayi1 < sayi2:
    print("Sayı1, sayı2'den küçüktür")
    print("Hala if bloğunun içerisindeyim")
#eğer if bloğuna girmez ise
elif sayi1 == sayi2:
    print("İki sayı eşittir")
#eğer if ve elif bloklarından hicbirine girmez ise
else:
    print("Sayı1 sayı2 den büyüktür.")

print("Burası if bloğunun dışıdır.")
















