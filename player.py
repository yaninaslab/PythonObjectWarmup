import fighter as f


class Player(f.Fighter):
    # def __init__(self, current_hp):
    #     self.current_hp = current_hp

    def attack(self, atk):
        if(atk == '1'):
            return 4
        elif(atk == '2'):
            return 5
        else:
            return 0

    # def get_attacked(self, dmg):
    #     self.current_hp = self.current_hp - dmg
