kilo = float(input("Lütfen kilonuzu giriniz"))
boy = float(input("Lütfen boyunuzu giriniz"))
vke = (kilo/boy**2)

if vke < 18.5:
    print("Zayıf")
elif vke>18.5 and vke<24.9:
    print("Normal")
elif vke>25.0 and vke<29.9:
    print("Fazla Kilolu")
elif vke>30 and vke<39.9:
    print("Şişman")
elif vke>40.0:
    print("Obez")
