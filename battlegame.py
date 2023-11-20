"""

battlegame.py
by Eric Jerde
09/30/2023
"""
import sys

# Task 1 Variable assignment
wizard = "Wizard"
human = "Human"
elf = "Elf"
orc = "Orc"
dragon = "Dragon"

# hp assignment
wizard_hp = 70
human_hp = 150
elf_hp = 100
orc_hp = 120
dragon_hp = 300

# damage assignment
wizard_damage = 150
human_damage = 20
elf_damage = 100
orc_damage = 120
dragon_damage = 50

# Task 2/ 3 input

while True:
    print("1)  " + wizard)
    print("2)  " + human)
    print("3)  " + elf)
    print("4)  " + orc)
    print("-" * 20 + "\n")
    choice = input("Choose your character:")
    print()
    if choice == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif choice == "2":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif choice == "3":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif choice == "4":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif choice == "Exit":
        sys.exit()

    else:
        print("Unknown Character")


print("The " + character, "was Selected")
print(f"HP: {my_hp}")
print(f"Damage: {my_damage}")
print()

# Task 4 Dragon Battle!
while True:
    dragon_hp -= my_damage
    print("The " + character, "damaged the Dragon!")
    print("The Dragon's HP is now:" + str(dragon_hp))
    print()
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break

    my_hp -= dragon_damage
    print("The Dragon strikes at", character)
    print(f"The {character}'s HP is now {my_hp}")
    print()
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break
