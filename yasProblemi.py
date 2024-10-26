yas = int(input("Yaşinizi girin? "))

okumadurumu = input("Okuyormusunuz? (evet : e ,hayır : h)")
if yas >=18 and okumadurumu == "h" :
    print("Askere gelme yaşınız geldi")

elif yas >=18 and okumadurumu == "e" :
    print("Okuunuz bittiğinde askere geleceksiniz")
 
else :
    print("Askere gelmek için zamanınız var") 