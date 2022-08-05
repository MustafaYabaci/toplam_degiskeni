toplam=0
while True:
    islem = (input("lütfen bir sayı giriniz"))
    if (islem == "q"):
        print("işlem sonlandırıldı")
        break
    islem=int(islem)
    toplam += islem
    print("girdiginiz sayıların toplamı",toplam)







