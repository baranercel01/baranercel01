print("Yukseklik ve genislik degerlerini giriniz")
yukseklik , genislik = int(input()) , int(input())
print("Karakter giriniz")
karakter = input()
for i in range(yukseklik):
    if i == 0 or i == yukseklik -1:
        print(karakter * genislik)
    else:
        print(karakter + (genislik-2)*" " + karakter)
