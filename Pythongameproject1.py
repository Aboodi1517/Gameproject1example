from random import random, randint

Swordsmanstats = {
    'health': 100,
}
Guardianstats = {
    'health': 150,
}
Thiefstats = {
    'health': 75,
}

enemystats = {
    'health': randint(50, 80),
}

def battleencounterswordsman():
    global enemyname
    while Swordsmanstats['health'] > 0 and enemystats['health'] > 0:
        action = input("What will you choose to do? 1. Attack 2. Defend 3. Flee ")
        print(Swordsmanstats, enemystats)
        if action == '1':
            print(f"You chose to attack {enemyname}. It dealt {randint(5, 10)} damage!")
            enemystats['health'] -= randint(5, 10)
            print("Enemy health is now:", enemystats['health'])
            print("It fought back, dealing " + f"{randint(5, 10)}" + " damage!")
            Swordsmanstats['health'] -= randint(5, 10)
            print("Health is now:", Swordsmanstats['health'])
        elif action == '2':
            print(f"You chose to defend against {enemyname}. Damage taken is {randint(0, 5)}!")
            Swordsmanstats['health'] -= randint(0, 5)
            print("Health is now:", Swordsmanstats['health'])
        elif action == '3':
            flee_result = randint(1,2)
            if flee_result == 1:
                print("You successfully fled from the battle!")
                break
            else:
                print("You failed to flee and the enemy attacks! You lost " + f"{randint(5, 15)}" + " health points.")
                Swordsmanstats['health'] -= randint(5, 15)
                print(Swordsmanstats)
        else:
            print("Invalid choice.")
        if Swordsmanstats['health'] <= 0:
            print('You have been defeated. Game Over.')
            break
        if enemystats['health'] <= 0:
            print(f"You have defeated {enemyname}!")
            break

def battleencounterguardian():
    global enemyname
    while Guardianstats['health'] > 0 and enemystats['health'] > 0:
        action = input("What will you choose to do? 1. Attack 2. Defend 3. Flee ")
        print(Guardianstats, enemystats)
        if action == '1':
            print(f"You chose to attack {enemyname}. It dealt {randint(0,5)} damage!")
            enemystats['health'] -= randint(0, 5)
            print("Enemy health is now:", enemystats['health'])
            print("It fought back, dealing " + f"{randint(5, 10)}" + " damage!")
            Guardianstats['health'] -= randint(5, 10)
            print("Health is now:", Guardianstats['health'])
        elif action == '2':
            print(f"You chose to defend against {enemyname}. Damage taken is 0!")
            Guardianstats['health'] -= 0
            print("Health is now:", Guardianstats['health'])
        elif action == '3':
            flee_result = randint(1,2)
            if flee_result == 1:
                print("You successfully fled from the battle!")
                break
            else:
                print("You failed to flee and the enemy attacks! You lost " + f"{randint(0,5)}" + " health points.")
                Guardianstats['health'] -= randint(0, 5)
                print(Guardianstats)
        else:
            print("Invalid choice.")
        if Guardianstats['health'] <= 0:
            print('You have been defeated. Game Over.')
            break
        if enemystats['health'] <= 0:
            print(f"You have defeated {enemyname}!")
            break

def battleencounterthief():
    global enemyname
    while Thiefstats['health'] > 0 and enemystats['health'] > 0:
        action = input("What will you choose to do? 1. Attack 2. Defend 3. Flee ")
        print(Thiefstats, enemystats)
        if action == '1':
            print(f"You chose to attack {enemyname}. It dealt {randint(10, 20)} damage!")
            enemystats['health'] -= randint(10, 20)
            print("Enemy health is now:", enemystats['health'])
            print("It fought back, dealing " + f"{randint(5, 10)}" + " damage!")
            Thiefstats['health'] -= randint(5, 10)
            print("Health is now:", Thiefstats['health'])
        elif action == '2':
            print(f"You chose to defend against {enemyname}. Damage taken is {randint(0, 7)}!")
            Thiefstats['health'] -= randint(0, 7)
            print("Health is now:", Thiefstats['health'])
        elif action == '3':
            flee_result = randint(1,2)
            if flee_result == 1:
                print("You successfully fled from the battle!")
                break
            else:
                print("You failed to flee and the enemy attacks! You lost " + f"{randint(10, 20)}" + " health points.")
                Thiefstats['health'] -= randint(10, 20)
                print(Thiefstats)
        else:
            print("Invalid choice.")
        if Thiefstats['health'] <= 0:
            print('You have been defeated. Game Over.')
            break
        if enemystats['health'] <= 0:
            print(f"You have defeated {enemyname}!")
            break

Name = input('What is your name?')
print('Hello, ' + Name + '!' ' Welcome to this game of fate')
print('Pick your class, challenger, from these list of choices\n 1. Swordsman\n 2. Guardian\n 3. Thief')
class_choice = input('Enter the number of your choice: ')
if class_choice == '1' or class_choice.lower() == 'swordsman':
    print('You have chosen the path of the Swordsman, a master of blade and combat.')
    player_class = 'Swordsman'
elif class_choice == '2' or class_choice.lower() == 'guardian':
    print('You have chosen the path of the Guardian, a stalwart defender and protector.')
    player_class = 'Guardian'
elif class_choice == '3' or class_choice.lower() == 'thief':
    print('You have chosen the path of the Thief, a cunning and agile trickster.')
    player_class = 'Thief'
else:
    print("Invalid class choice, try again")
    exit()

print('Now, where shall you spawn? Pick a location from these 2 choices\n 1. Fairy Forest\n 2. Dracula\'s Castle')
spawn_choice = input('Enter the number of your choice: ')

fairyforest = False
draculascastle = False
battleencounter = False
enemyname = ""

if spawn_choice == '1' or spawn_choice.lower() == 'fairy forest':
    fairyforest = True
    print('You have spawned in the mystical Fairy Forest, filled with magical creatures and enchanting flora. Be careful, their demeanor is far more evil than it appears.')
elif spawn_choice == '2' or spawn_choice.lower() == 'dracula\'s castle':
    draculascastle = True
    print('You have spawned in the ominous Dracula\'s Castle, a place of dark magic and ancient secrets. Beware of the lurking dangers within its walls.')
else:
    print("Invalid spawn choice")
    exit()

if draculascastle:
    print('As you explore the eerie halls of Dracula\'s Castle, a shadowy figure emerges from the darkness. It\'s a vampire, its eyes glowing with hunger as it prepares to attack.')
    choice = input('Do you want to (1) Confront the vampire or (2) Hide and wait? ')
    if choice == '1':
        print('The vampire is hostile and attacks you!')
        enemyname = 'Vampire'
        battleencounter = True
    elif choice == '2':
        rand_val = randint(1,2)
        if rand_val == 1:
            print('You successfully hid from the vampire and it moves on.')
        elif rand_val == 2:
            print('You failed to hide and the vampire attacks you!')
            enemyname = 'Vampire'
            battleencounter = True

if fairyforest:
    print('As you venture deeper into the Fairy Forest, you encounter a mischievous fairy blocking your path. She giggles and flutters her wings, ready to play a trick on you.')
    choice = input('Do you want to (1) Approach the fairy or (2) Sneak around her? ')
    if choice == '1':
        print('The fairy is hostile and attacks you!')
        battleencounter = True
        enemyname = 'Hostile Fairy'
    elif choice == '2':
        rand_val = randint(1,2)
        if rand_val == 1:
            print('You successfully sneak around the fairy and continue your journey.')
        elif rand_val == 2:
            print('You failed to sneak around the fairy and she attacks you!')
            enemyname = 'Hostile Fairy'
            battleencounter = True

if battleencounter:
    if player_class == 'Swordsman':
        battleencounterswordsman()
    elif player_class == 'Guardian':
        battleencounterguardian()
    elif player_class == 'Thief':
        battleencounterthief()