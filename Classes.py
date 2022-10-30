class Akatsuki:
    def __init__(self, name, location):
        self.name = name
        self.location = location 
    
    def details(info):
        print('\nName: ', info.name)
        print('Location: ', info.location)
        
    def skill_1(ability_1):
        print(ability_1.name + ' uses conceal.')
    
    def skill_2(ability_2):
        print(ability_2.name + ' uses Amaterasu.')
        
print('---------------AKATSUKI MEMBERS--------------' )
member1 = Akatsuki("Deidara", "Iwagakure")
member1.details()

member2 = Akatsuki("Hidan", "Yugakure")
member2.details()

member3 = Akatsuki("Itachi", "Konohagakure")
member3.details()
member3.skill_2()

member4 = Akatsuki("Kakuzu", "Takigakure")
member4.details()

member5 = Akatsuki("Kisame", "Kirigakure")
member5.details()

member6 = Akatsuki("Konan", "Amegakure")
member6.details()

member7 = Akatsuki("Nagato", "Amegakure")
member7.details()

member8 = Akatsuki("Orochimaru", "Konohagakure")
member8.details()

member9 = Akatsuki("Sasori", "Sunagakure")
member9.details()

member10 = Akatsuki("Tobi", "Konohagakure")
member10.details()
member10.skill_1()