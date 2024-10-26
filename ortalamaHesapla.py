def ortalama_hesapla() :
    print("1.sinavinizin notunu giriniz? ")
    sinav1 = input()
    print("2.sinavinizin notunu giriniz? ")
    sinav2 = input()
    print("Proje sinavinin notunu giriniz")
    proje = input()
    ortalama = (int(sinav1) + int(sinav2) + int(proje)) / 3
    print("Bu dönemdeki ortalamaniz " + str(ortalama))
    if int(ortalama) < 50 :
        print("Bu donem dersten kaldiniz diğer dönem daha azimli bir calismayla daha iyi sonuclar alabilirsiniz")

    if int(ortalama) == 50 :
        print("Bu donem kil payi kurtardiniz daha fazla azimle rahatca gecebilirsiniz sinifi ")   
    if int(ortalama) > 50 :
        print("Tebrikler sinifi gectiniz daha buyuk basarilara imza atmaniz dilegiyle")     
     

ortalama_hesapla()


