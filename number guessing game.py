import random
import time

print("*"*30)

print("sayı tahmin oyunu\n1' ile 40 arasında",)

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = int(input("tahmininiz:\t"))

    if (tahmin < rastgele_sayı) :
        print("Bakalım doğrumu...")
        time.sleep(1)

        print("Daha yüksek bir sayı söyleyin...\n")
        tahmin_hakkı -= 1

    elif (tahmin > rastgele_sayı) :
        print("Bakalım doğrumu...")
        time.sleep(1)

        print("Daha düşük bir sayı söyleyin...\n")
        tahmin_hakkı -= 1

    else:
        print("Bakalım doğrumu...")
        time.sleep(1)
        print("Doğru tahmin",rastgele_sayı)
        print("Congratulations")
        break

    if (tahmin_hakkı == 0) :
        print("Tahmin hakkınız bitmiştir.")
        break