#sınıflar -> classlar
#modules
#paket yönetimi

class Human:
    name = "Halit"
    #built-in
    #constructor
    #initialize
    def __init__(self):
        print("Bir human instance'ı üretildi")

    def talk(self, sentence):      #self yerine baska bir parametre de yazabılırız.
        name= "Ercan "
        print(f"{self.name}: {sentence}")
    def walk(self):
        print("Human is walking")
    
#instance -> ornek
human1 = Human()
human1.talk("Merhaba")
human1.walk()

human2 = Human() #--> human class'ından oluşmuş iki obje human1 ve human2
human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)
 
