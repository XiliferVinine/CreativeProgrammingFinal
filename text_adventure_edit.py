
import random


def text_adventure():
    stuff = ['water', 'food', 'sword']
    party = ['you']
    pos_x = 2
    pos_y = 2
    you_hp = 15.0

    map_dungeon = '''
                           ----------------
                           |              |__
                           |   main room  |__  outside
                        == |              |
        --------------- ==  ------|   |-----
        |             |==         |   | 
        |  downstairs |       ----     ----
        |             |      |   armory    |
        --  -----------       -------------
          |  |
        --|  |-------______---------------
        |  cellar   |______| locked room |
        -------------      ---------------
    '''

    def d_intro():
        print("\nYou have travelled countless miles and faced many dangers to finally reach this dungeon. Inside, a "
              "terrifying beast has kidnapped the prince/princess but, you will save them!")

    def check_items(item):
        x = 0
        have = False
        for i in range(len(stuff)):
            x += 1
            if stuff[x - 1] == item:
                have = True
            else:
                pass
        return have

    def check_pos():
        global pos_x
        global pos_y
        if pos_x < 0:
            print("Hey, you stepped out of the world. I'll put you back")
            pos_x = 0
        if pos_y < 0:
            print("Hey, you stepped out of the world. I'll put you back")
            pos_y = 0
        if pos_x > 2:
            print("Wow! You're just going to leave, what a crappy hero...")
            quit()
        if pos_y > 3:
            print("Hey, you stepped out of the world. I'll put you back")
            pos_y = 3

    def search():
        num_items = len(stuff)
        if num_items < 7:
            i = random.randint(0, 15)
            if i == 0 or 3:
                print("you found some water")
                stuff.append('water')
            elif i == 1 or 5:
                print("you found some floor food, YUMMY!")
                stuff.append('food')
            elif i == 2:
                w = random.randint(0, 2)
                if w == 0:
                    print("you found a whip")
                    stuff.append('whip')
                elif w == 1:
                    print("you found a club")
                    stuff.append('club')
                elif w == 2:
                    print("you found a holy sword")
                    stuff.append('hsword')
            else:
                print("you found nothing special")
        else:
            print("you can't carry anything else. Try dropping something or cheating the carry weight stats...")

    def drop():
        print(stuff)
        drop_item = input("\nEnter the index of the item you wish to drop using the number keys "
                          "(hint: the first item is index 0)")
        stuff.pop(int(drop_item))

    def fight():

        global you_hp

        you_attack = 5.0
        you_defense = 7.0
        zombie_attack_one = 5.0
        zombie_defense_one = 4.0
        zombie_hp_one = 7.0
        zombie_defense_two = 6.0
        zombie_hp_two = 7.0

        have = check_items('whip')
        if have == True:
            you_attack += 1.5
            you_defense += 0.5
        have = check_items('stick')
        if have == True:
            you_attack += 2.0
            you_defense -= 0.5
        have = check_items('hsword')
        if have == True:
            you_attack += 4.0
            you_defense += 1.0
        else:
            pass

        num_zombies = random.randint(1, 2)
        turn = 0
        fight = True
        print("watch out, there are " + str(num_zombies) + " zombies!")

        while fight == True:
            turn += 1
            go = turn % 2

            if num_zombies == 1:
                zombie_hp_two = 0
            else:
                pass

            if zombie_hp_one <= 0 and zombie_hp_two <= 0:
                print("you defeated them!")
                break
            if you_hp <= 0:
                print("You FAILED, the prince/princess is dragon food")
                quit()

            if go == 1:
                super_att = random.randint(1, 7)
                if super_att == 1:
                    you_attack = 15.0
                elif super_att == 2:
                    you_attack = 10.0
                elif super_att == 3:
                    you_attack = 30.0
                elif super_att == 4:
                    you_attack = 1.0
                else:
                    you_attack = 5.0

                opt = input("do you wish to attack\n")
                if opt == 'yes':
                    dev = input("which zombie would you like to attack\n")
                    if dev == "1":
                        hit = you_attack / zombie_defense_one
                        zombie_hp_one -= hit
                        print("zombie one has " + str(int(zombie_hp_one)) + " hp left")
                    elif dev == "2":
                        hit = you_attack / zombie_defense_two
                        zombie_hp_two -= hit
                        print("zombie two has " + str(int(zombie_hp_two)) + " hp left")
                    else:
                        print("invalid input -> lose a turn")
                elif opt == 'run':
                    r = random.randint(0, 5)
                    if r == 0:
                        print("you got away safely!")
                        break
                    else:
                        print("sadly you were not agile enough to escape the zombies")
                        pass
                else:
                    print("Invalid input. lose a turn")

            elif go == 0:
                att = random.randint(1, 5)
                super_att = random.randint(1, 3)
                if super_att == 1:
                    zombie_attack_one = 20.0
                elif super_att == 2:
                    zombie_attack_one = 2.0
                else:
                    zombie_attack_one = 6.0

                if att == 1 or 2 or 3:
                    hit = zombie_attack_one / you_defense
                    you_hp -= hit
                    print("\n a zombie attacked and you have " + str(int(you_hp)) + " hp left")
                else:
                    print("\nThe Zombie misses you")

    def main():

        global pos_x
        global pos_y
        global you_hp

        d_intro()

        game = True
        while game == True:
            z = random.randint(0, 3)
            if z == 3:
                fight()
            check_pos()
            dev = input("\nWhat are you going to do?\n").lower()

            if dev == "quit":
                game = False
            elif dev == "left":
                pos_x -= 1
            elif dev == "right":
                pos_x += 1
            elif dev == "up":
                pos_y += 1
            elif dev == "down":
                pos_y -= 1
            elif dev == "pos x":
                print(pos_x)
            elif dev == "pos y":
                print(pos_y)
            elif dev == "map":
                if pos_x <= 2 and pos_y <= 3:
                    print(map_dungeon)
                    if pos_x == 0 and pos_y == 0:
                        print("you are in the cellar")
                    elif pos_x == 1 and pos_y == 0:
                        print("you are in the *locked* room")
                    elif pos_x == 0 and pos_y == 1:
                        print("you are downstairs")
                    elif pos_x == 0 and pos_y == 2:
                        print("you are downstairs")
                    elif pos_x == 1 and pos_y == 2:
                        print("you are in the main room")
                    elif pos_x == 1 and pos_y == 1:
                        print("you are in the armory")
                    elif pos_x == 1 and pos_y == 3:
                        print("you are in the main room")
                    elif pos_x == 2:
                        print("you are outside the dungeon")
                else:
                    print("no  map... \nTry moving up or down!\n")
            elif dev == "check items":
                print(stuff)
            elif dev == "health":
                print(you_hp)
            elif dev == "drink":
                have = check_items('water')
                if have == True:
                    hp_up = random.randint(2, 6)
                    you_hp += hp_up
                    stuff.remove('water')
                    print("your hp increased by " + str(hp_up))
                elif have == False:
                    print("you don't have any water...sucks for you. *narrator takes sip of water*")
                else:
                    print("something went horribly wrong")
            elif dev == "eat":
                have = check_items("food")
                if have == True:
                    hp_up = random.randint(4, 8)
                    you_hp += hp_up
                    stuff.remove('food')
                    print("your hp has increased by " + str(hp_up))
                elif have == False:
                    print("you don't have any food... :(")
                else:
                    print("something went horribly wrong")
            elif dev == "search":
                search()
            elif dev == "drop":
                drop()
            else:
                print("what is this \"" + dev + "\" nonsense?")

    print(
        "\n\n\n\n Hello and welcome to the adventure hero!\n If this is your first time playing, you should type in 'how "
        "to 'play' so that you can learn to play the game. \nIf you have played the game before, know the game's code, or "
        "are just really lucky, type in 'start' to begin or 'quit' to exit.")
    opt = input()
    if opt == 'start':
        main()
    elif opt == 'how to play':
        print(
            "\n\n\n\nHOW TO PLAY: \n\n MAIN CONTROLS: There are multiple things you can do in this game. To move around "
            "you simply enter which way you want to go. For example, if you want to go left, type in \"left\". "
            "\nIt is importanr to note that your movement is tracked in a grid system, you can find your position at any "
            "time by typing \"pos x\" or \"pos y\".\n To print the map so you can see where your are, input \"map\". To "
            "see what you are holding, input \"check items\" and to drop an item, input \"drop\".\n You can also look for "
            "items by inputting \"search\".\n If you want to know how many health points you have, type \"health\". \n\n "
            "FIGHTING: You can also fight in this game. First you will be told how many enemies you are facing and then "
            "you can choose to fight by typing \"yes\" or try to run by typing \"run\".\n To choose which enemy to attack, "
            "type the number of the enemy, for example, \"1\" for enemy one or \"2\" for enemy 2. \n If your hp is low "
            "after fighting, you can eat or drink to restore hp by typing \"eat\" or \"drink\", but you need the items "
            "to do so. \n That's it, HAVE FUN!")
        if input() == 'start':
            main()
        elif input() == 'quit':
            exit
    else:
        print("Sorry, seems a black hole has opened in the game's source code. Shutting Down...")


