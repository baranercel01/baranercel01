print("Baklava diliminin orta satirindaki yildiz sayisini giriniz ")
ortaSatirYildiz = int(input())
boslukSayisi = ortaSatirYildiz + 2
print("Baklava dilimini hangi karakterden yapmak istediğinizi giriniz ")
baklava_karakter = input()
for i in range(1,ortaSatirYildiz + 1) :
    for j in range(boslukSayisi):
        print(end=" ")
    boslukSayisi -= 1
    for j in range(i):
        print(end=baklava_karakter + " ")
    print()
boslukSayisi += 2
for i in range(ortaSatirYildiz - 1 , 0 , -1):
    for j in range(boslukSayisi) :
         print(end=" ")
    boslukSayisi += 1
    for j in range(i) :
         print(end=baklava_karakter + " ")
    print()