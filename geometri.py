import math


print("Merhaba geometri uygulamasina hosgeldiniz ")
print("Hangi isslemi yapmak istediginizi seciniz ")
print("Ucgen  : U , Kare :  K  , Cember : C , Dikdortgen : D")

def ucgen() :
    print("Lütfen hangi islemi yapmak istediginizi seciniz ")
    print("Alan hesaplama : a , Cevre hesaplama : c ")
    secenek = input()
    def ucgen_alan():
        print("Lutfen ucgenin bir ic acısını soyleyiniz ")
        derece = float(input())
        print("Lutfen yazdiginiz aciya komsu olan iki kenarin uzunlugunu yaziniz ")
        kenar1 = float(input())
        kenar2 = float(input())
        radyan = math.radians(derece)
        alan = 1/2 * math.sin(radyan) * kenar2 * kenar1
        print("Yazdiginiz ucgenin alanı = " + str(alan))
    def ucgen_cevre():
        print("Lutfen ucgeninizin kenar uzunluklarini giriniz ")
        kenar1 = float(input())
        kenar2 = float(input())
        kenar3 = float(input())
        cevre = kenar1 + kenar2 + kenar3
        print("Girdginiz ucgenin cevresi  = " + str(cevre))


    if secenek == "a" :
        ucgen_alan()
    elif secenek == "c" :
        ucgen_cevre()
    else :
        print("Hatali giris !!! ")
        print("Uygulamayi tekrardan baslatiniz ")
def kare():
    print("Lütfen hangi islemi yapmak istediginizi seciniz ")
    print("Alan hesaplama : a , Cevre hesaplama : c ")
    secenek = input()
    def kare_alan():
        print("Lutfen islem yapmak istediginiz karenin kenar uzunlugunu giriniz ")
        kenar_uzunluk = float(input())
        alan = kenar_uzunluk ** 2
        print("Kenar uzunlugunu girdiginiz karenin alani = " + str(alan))
    def kare_cevre():
        print("Lütfen islem yapmak istediginiz karenin kenar uzunlugunu giriniz ")
        kenar_uzunluk = float(input())
        cevre = kenar_uzunluk * 4
        print("Uzunlugunu girdiginiz karenin cevresi = " + str(cevre))
    if secenek == "a" :
        kare_alan()
    elif secenek == "c" :
        kare_cevre()
    else :
        print("Hatali giris. Uygulamayi tekrar baslatiniz" )
def cember() :
    print("Lütfen hangi islemi yapmak istediginizi seciniz ")
    print("Alan hesaplama : a , Cevre hesaplama : c ")
    secenek = input()
    pi = 3.14
    def cember_alan() :
        print("Lütfen islem yapmak istediginiz cemberin yaricap uzunlugunu giriniz ")
        yaricap = float(input())
        alan = pi * (yaricap**2)
        print("İslem yaptiginiz cemberin alani = " + str(alan))
    def cember_cevre():
        print("Lutfen islem yapmak istediginiz cemberin yaricap uzunlugunu giriniz ")
        yaricap = float(input())
        cevre = 2 * pi * yaricap
        print("İslem yaptiginiz cemberin cevresi = " + str(cevre))
    if secenek == "a" :
        cember_alan()
    elif secenek == "c" :
        cember_cevre()
    else :
        print("Hatali giris yaptiniz ")
        print("uygulamai tekrar baslatiniz ")
def dikdortgen():
    print("Lütfen hangi islemi yapmak istediginizi seciniz ")
    print("Alan hesaplama : a , Cevre hesaplama : c ")
    secenek = input()
    def dikdortgen_alan():
        print("Lutfen islem yapmak istediginiz dikdortgenin kenar uzunluklarını giriniz ")
        kenar1 = float(input())
        kenar2 = float(input())
        alan = kenar1 * kenar2
        print("İslem yaptginiz dikdortgenin alanı = " + str(alan))
    def dikdortgen_cevre():
        print("Lutfen islem yapmak istediginiz dikdortgenin kenar uzunluklarını giriniz ")
        kenar1 = float(input())
        kenar2 = float(input())
        cevre = (kenar1 * 2) + (kenar2 * 2)
        print("İslem yaptiginiz dikdortgenin cevresi = " + str(cevre))
    if secenek == "a" :
        dikdortgen_alan()
    elif secenek == "c" :
        dikdortgen_cevre()
    else :
        print("Hatali giris yaptiniz")
        print("Uygulamayi tekrardan baslatiniz")

def islem():
    while True:
        try:
            islem = input()
            if islem == "U":
                ucgen()
            elif islem == "K":
                kare()
            elif islem == "C":
                cember()
            elif islem == "D":
                dikdortgen()
            else:
                print("Hatalı giriş, lütfen geçerli bir şekil girin.")
        except Exception as e:
            print(f"Hata oluştu: {e}")
islem()