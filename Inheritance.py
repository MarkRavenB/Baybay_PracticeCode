#single inheritance

#base class
class Gamer1:
    def game1(self):
        print('I\'m a Gamer.')

#derived class        
class Gamer2(Gamer1):
    def game2(self):
        print('I\'m also a Gamer.')

Player = Gamer2()
Player.game1()
Player.game2()

class GenshinImpact:
    genshinID = ''
    
    def ID(self):
        print(self.genshinID)

class TowerOfFantasy:
    UID = ''
    
    def tofID(self):
        print(self.UID)
        
class Player(GenshinImpact, TowerOfFantasy):
    def Games(self):
        print('Genshin ID: ', self.genshinID)
        print('TOF ID: ', self.UID)
        
P1 = Player()
P1.genshinID = '254999'
P1.UID = '16000009'
P1.Games()