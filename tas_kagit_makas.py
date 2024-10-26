
import random

secenekler = ["Tas", "Kagit", "Makas"]

while True:
    print("Lütfen taş, kağıt veya makastan birini seçin (çıkmak için 'cikis' yazın): ")
    print("Taş = Tas , Kagit = Kagit , Makas = Makas")
    oyuncununsecimi = input()

    if oyuncununsecimi == "cikis":
        print("Oyundan çıkış yapıldı.")
        break

    if oyuncununsecimi not in secenekler:
        print("Yanlış seçim yaptınız, lütfen tekrar deneyiniz.")
        continue

    bilgisayarınsecimi = random.choice(secenekler)
    print(f"Bilgisayarın seçimi: {bilgisayarınsecimi}")

    if oyuncununsecimi == bilgisayarınsecimi:
        print("Oyun Berabere")
    elif (oyuncununsecimi == "Tas" and bilgisayarınsecimi == "Makas") or \
         (oyuncununsecimi == "Kagit" and bilgisayarınsecimi == "Tas") or \
         (oyuncununsecimi == "Makas" and bilgisayarınsecimi == "Kagit"):
        print("Oyuncu kazandı")
    else:
        print("Bilgisayar kazandı")
