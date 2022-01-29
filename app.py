from operator import add
#import inputexception as ie
import player as p
import computer as c
import dbcreds
import mariadb as db
import dbqueries as dbq


print("Hey there! Welcome to the fighting game!")
player = p.Player(10)
comp = c.Computer(10)
db = dbq.DbInteraction()

db.dislay_record()
while(True):
    print(f"Player HP: {player.current_hp} -- Computer HP: {comp.current_hp}")
    selection = input("Please select 1 for high attack and 2 for low attack: ")

    # if(selection != '1' and selection != '2'):
    #     raise ie.InvalidInput()

    dmg = player.attack(selection)
    comp.get_attacked(dmg)
    print(f"Player hits the computer for {dmg} points!")
    if(comp.current_hp <= 0):
        print("Game Over, you win!")
        db.add_win_loss_to_db(1)
        exit()

    dmg = comp.attack()
    player.get_attacked(dmg)
    print(f"Computer hits the player for {dmg} points!")
    if(player.current_hp <= 0):
        print("Game Over, you lose!")
        db.add_win_loss_to_db(0)
        exit()

    print("-------------------------------------")
