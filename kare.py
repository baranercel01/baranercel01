print("Yukseklik ve genislik degerlerini giriniz")
yukseklik , genislik = int(input()) , int(input())
print("Karakter giriniz")
karakter = input()
for i in range(yukseklik):
    print(karakter*genislik)