age = int(input("Yoshni kiriting: "))
gender = input("Jinsingizni kiriting (erkak/ayol): ").lower()

if age < 0:
    print("Bunday yosh bo‘lishi mumkin emas")

elif age <= 3:
    print("Bu bola hali juda yosh")

elif age <= 6:
    print("Bu bola bog‘cha yoshida")

elif age <= 18:
    print("Bu bola maktabda o‘qiydi")

elif age <= 22:
    print("Bu yosh talaba bo‘lishi mumkin")

elif age <= 60:
    if gender == "erkak":
        print("Bu erkak ishlash yoshida")
    elif gender == "ayol":
        print("Bu ayol ishlash yoshida")
    else:
        print("Jins noto‘g‘ri kiritildi")

elif age <= 110:
    print("Bu inson pensioner")

else:
    print("Bunday yosh mavjud emas")
