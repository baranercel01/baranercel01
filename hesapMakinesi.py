number1 = int(input("İşlem yapmak istediğiniz ilk sayiyi giriniz? "))
number2 = int(input("İşlem yapmak istediğiniz ikinci sayiyi giriniz? "))

islem = input("""yapmak istediğiniz işlmei seçiniz
              (Toplama: + , Çıkarma: - , Çarpma: * , Bölme: / )""")

if islem == "+":
    print("Sonuç: "+str(number1+number2))
elif islem == "-":
    print("Sonuç: "+str(number1-number2))
elif islem == "*":
    print("Sonuç: "+str(number1*number2))
elif islem == "/":
    print("Sonuç: "+str(number1/number2))            
