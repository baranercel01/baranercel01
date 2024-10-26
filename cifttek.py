print("Bir sayi giriniz")
girilensayi = int(input())

if girilensayi > 0 and girilensayi %2 == 0 :
    print("Bu sayi cift bir pozitif sayidir")
elif girilensayi > 0 and girilensayi %2 == 1 :
    print("Bu sayi tek bir pozitif sayidir")
elif girilensayi < 0:
    print("Bu sayi negatiftir")
else:
    print("Bu sayi sifirdir")
