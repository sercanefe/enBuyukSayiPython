# -*- coding: utf-8 -*-

sayi1 = int(input("Sayı Giriniz (1.)"))
sayi2 = int(input("Sayı Giriniz (2.)"))
sayi3 = int(input("Sayı Giriniz (3.)"))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En Büyük Sayı = ",enBuyuk)