import random
print("Uygulamamiza hosgeldiniz :) ")
print("Sizin icin ne yapabiliriz ? "
      "video begenilme orani : begeni  "
      "okul ortalamasi hesaplama : ortalama  "
      "tas kagit makas : oyun ")
uygulama_secenekleri = input()
def begeni_orani():
    print("Lütfen videonun like sayisini giriniz ")
    like = float(input())
    print("Lütfen videonun dislike sayisini giriniz ")
    dislike = float(input())
    begenilme_orani = (like / ( like + dislike)) * 100
    print(begenilme_orani)
    if begenilme_orani > 80 :
        print("Videonuzun izlenme oranı gayet iyi")
    elif begenilme_orani > 50 :
        print("Videonuzun izlenme orani iyi derecede ")
    elif begenilme_orani == 50 :
        print("Videonuzun izlenme orani orta derecede ")
    elif begenilme_orani < 50 :
        print("Videonuzun izlenme orani kotu seviyede ")
    elif begenilme_orani < 20 :
        print("Videonuzun izlenme oranı vasat derecede SİLİNN!!!  ")
    else :
        print("Yapabilecegim baska bisey varmı efendim ")

def okul_ortalamasi():
    print("Lutfen ilk sinavinizin not degerini sayıyla giriniz ")
    exam1 = float(input())
    print("Lutfen ikinci sinavinizin not degerini sayiyla giriniz ")
    exam2 = float(input())
    print("Lutfen proje sinavinizin not degerini giriniz ")
    exam3 = float(input())
    ortalama = (exam1 + exam2 + exam3) / 3
    print("Karne ortalamaniz " + str(ortalama))
    if ortalama > 85 :
        print("Sinifi takdir belgesi ile gectiniz TEBRIKLER ")
    elif ortalama >70 :
        print("Sinifi tesekkur belgesi ile gectiniz daha iyi calismalar :)  ")
    elif ortalama > 50 :
        print("Sinifi herhangi bi belge almadan bitirdiniz ")
    else :
        print("Maalesef sinifi gecemediniz ")

def tas_kagit_makas():
    secenekler = ["Tas" , "Kagit" , "Makas"]
    print("Tas kagit makas oyununa hosgeldiniz"
          "Oyunun kuralları :  tas makası , makas kagiti , kagitta tası yener...")
    print("Lutfen bi hamle seciniz "
          "taş : Tas , kağıt : Kagit , makas : Makas ")
    oyuncu_hamle = input()

    for i in secenekler:
        bilgisayarinsecimi = random.choice(secenekler)
    print(bilgisayarinsecimi)
    if oyuncu_hamle == "Tas" and bilgisayarinsecimi == "Tas":
        print("Oyun Berabere")

    elif oyuncu_hamle == "Tas" and bilgisayarinsecimi == "Makas":
        print("Oyuncu kazandı")

    elif oyuncu_hamle == "Tas" and bilgisayarinsecimi == "Kagit":
        print("Bilgisayar kazandı")

    elif oyuncu_hamle == "Makas" and bilgisayarinsecimi == "Kagit":
        print("Oyuncu kazandı")

    elif oyuncu_hamle == "Makas" and bilgisayarinsecimi == "Tas":
        print("Bilgisayar kazandı")

    elif oyuncu_hamle == "Makas" and bilgisayarinsecimi == "Makas":
        print("Oyun Berabere")

    elif oyuncu_hamle == "Kagit" and bilgisayarinsecimi == "Tas":
        print("Oyuncu kazandı")

    elif oyuncu_hamle == "Kagit" and bilgisayarinsecimi == "Makas":
        print("Bilgisayar kazandı")

    elif oyuncu_hamle == "Kagit" and bilgisayarinsecimi == "Kagit":
        print("Oyun Berabere")

    else:
        print("Yanlis secim yaptiniz lutfen programı yeniden baslatip dogru secim yapiniz")

if uygulama_secenekleri == "begeni" :
    begeni_orani()
elif uygulama_secenekleri == "ortalama" :
    okul_ortalamasi()
elif uygulama_secenekleri == "oyun" :
    tas_kagit_makas()
else :
    print("Yapabilcegim baska bisi yok maalesef ")