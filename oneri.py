#To Do List

sarki = ["Dedublüman" , "Koray Avci" , "Selda Bağcan" , "Ceza" , "Elmusto" , "Uzay" , "Uzi" ,]
yemek = ["Adana Kebap" , "Arnavut Ciğeri" , "Harput Köfte" , "Karniyarik" , "Taze Biber Dolmasi" , "Fellak Köftesi"]
pcoyunlari = ["Counter Strike 2" , "Valorant" , "The Finals" , "League of Legends" , "Dota 2" , "Metin 2"]
mobiloyunlar = ["Pubg Mobile" , "Call of Duty Mobile" , "Arena Breakout" , "Wild Rift" , "Mobile Legends"]

önerilistesi = input("""Lütfen hangisi hakkinda öneri almak istediğinizi seçiniz
      depresifsarkilar: ds , rap tarzi sarkilar: rs , etliyemek: ey , etsizyemek: esizy , fpspcoyunu: fpspcoyunu ,mmorpgpc: mmorpgpc ,
                     fpsmobiloyun: fpsmobil , mmorpgmobiloyun: mmorpgmobil  """)

if önerilistesi == "ds" :
    print(sarki[0:3])
elif önerilistesi == "rs" :
    print(sarki[3:7])    
elif önerilistesi == "ey" :
    print(yemek[0:4])    
elif önerilistesi == "esizy" :
    print(yemek[4:7])    
elif önerilistesi == "fpspcoyunu" :
    print(pcoyunlari[0:3])
elif önerilistesi == "mmorpgpc" :
    print(pcoyunlari[3:6])
elif önerilistesi == "fpsmobil" :
    print(mobiloyunlar[0:3])
elif önerilistesi == "mmorpgmobil" :
    print(mobiloyunlar[3:5])          
else :
    print("Ben sadece bu listeler için programlandim bu uygulamaya göz attığınız için teşekkürler:)")    