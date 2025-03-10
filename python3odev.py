
file_name = "kullanici_verileri.txt"


with open(file_name, "w", encoding="utf-8") as file:
    metin = input("Bir metin giriniz: ")
    file.write(metin + "\n")


with open(file_name, "r", encoding="utf-8") as file:
    print("\nDosya içeriği:")
    print(file.read())


with open(file_name, "w", encoding="utf-8") as file:
    print("\nLütfen 5 farklı satır veri girin:")
    for i in range(5):
        satir = input(f"{i+1}. satır: ")
        file.write(satir + "\n")


with open(file_name, "r", encoding="utf-8") as file:
    print("\nDosyanın satır satır içeriği:")
    for satir in file:
        print(satir.strip())