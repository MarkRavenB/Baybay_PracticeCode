class Genshin:
    def __init__(self):
        self.HP = int(input('Enter HP: '))
        self.ATK = int(input('Enter ATK: '))
        self.PyroDmgBonus = int(input('Enter Pyro Damage Bonus: '))

    def display(self):
        print('-------------HuTao Stats-------------')
        print('HP: ', self.HP)
        print('ATK: ', self.ATK)
        print('Pyro Damage Bonus: ', self.PyroDmgBonus)
        
    def skill(self):
        print('\n------------HuTao Uses Elemental Skill---------------')
        print('HuTao\'s HP decreases and ATK increases')
        self.HP = self.HP - (self.HP * 0.15)
        self.ATK = self.ATK + (self.ATK * 0.10)
        print('Current HP: ', self.HP)
        print('Current ATK: ', self.ATK)

HuTao = Genshin()


print('1. Display')
print('2. Initiate Skill')
user = False
while user == False:
    user = int(input('Enter Number: '))
    if user == 1:
        HuTao.display()
    elif user == 2:
        HuTao.skill()
    else:
        print('Exiting....Thank YOU, WELL DONEEEEE')
    user = False







        