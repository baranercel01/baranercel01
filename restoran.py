
adanakebap = 165
cigersis = 160
tavukkanat = 140
karisik = 180
kuzubonfile = 190

garson = input("""Restoranimiza hosgelediniz efendim buyurun menümüz. 
            Adana Kebap : a , Ciger Sis : c , Tavuk Kanat : t , Karisik : k , Kuzu Bonfile : kb """)
if garson == "a" :
    print("Buyurun efendim hesabiniz " + str(adanakebap) + "tl'dir")
elif garson == "c" :
    print("Buyurun efendim hesabiniz " + str(cigersis) + "tl'dir")
elif garson == "t" :
    print("Buyurun efendim hesabiniz " + str(tavukkanat) + "tl'dir")
elif garson == "k" :
    print("Buyurun efendim hesabiniz " + str(karisik) + "tl'dir")
elif garson == "kb" :
    print("Buyurun efendim hesabiniz " + str(kuzubonfile) + "tl'dir")
else :
    print("Maalesef menumuz bu yemeklerden olusuyor efendim baska yardimci olailecegim bisey varsa soyleyebilirsiniz ")                