
while True:

    minimum = int(input("Minimum Değer: "))
    if minimum <=0:
        print("Mükemmel sayılar negatif veya 0 olamaz")
    else:
        maksimum = int(input("Maksimum Değer: "))
    if maksimum <= minimum:
        print("Yanlış aralık belirlediniz")
    else:
        for sayı in range(minimum,maksimum):
            toplam = 0
            for b in range(1,sayı-1):
                if sayı % b == 0:
                    toplam += b
            if toplam == sayı:
                print(sayı)


