import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


# Introduction to the game.
def intro(enemies):
    global enemy
    enemy = random.choice(enemies)
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {enemy} is somewhere around "
                "here, and has been terrifying the nearby village.")


# The house scenario.
def house(enemies, weapons):
    print_pause("You walk towards the house")
    print_pause(f"Eep! The {enemy} opens the door!")
    print_pause("Please enter the number of the choice you're willing to make")
    choice = input(f"1. Fight the {enemy}\n"
                   "2. Run away!!")
    if '1' in choice:
        print_pause("You roll up your sleeves and...")
        if "sword" in weapons:
            print_pause("He sees your magic sword, he can't beat "
                        "that so he get scared and runs way")
            print_pause("YOU WIN!!!")
        else:
            print_pause(f"You try to fight the {enemy} "
                        "with your weak dagger..")
            print_pause("That wouldn't be enough")
            print_pause("Good effort but you lose.")
            play_again()
    elif '2' in choice:
        print_pause("You run so fast! No one seems to have followed you")
        play_again()
    else:
        print_pause("Invalid choice, try again please.")
        house(enemies, weapons)


# The cave scenario.
def cave(enemies, weapons):
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    if "sword" in weapons:
        print_pause("Nothing there, you go back to the field.")
        field(enemies, weapons)
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and "
                    "take the sword with you.")
        print_pause("You walk back out to the field.")
        weapons.append("sword")
        field(enemies, weapons)


# The field scenario.
def field(enemies, weapons):
    print_pause("You are on a crossway in the field.")
    print_pause("On your left is a house on your right "
                "a secret cave.\n")
    print_pause("Please enter a number to make a choice.")
    choice = input("1. Go to the house\n"
                   "2. Go to the cave\n")
    if choice == '1':
        house(enemies, weapons)
    elif choice == '2':
        cave(enemies, weapons)
    else:
        print_pause("Invalid choice, try again please.")
        field(enemies, weapons)


# Function that enables the player to decide whether to play the game again.
def play_again():
    choice = input("Do you want to play again y/n?\n").lower()
    if "y" in choice:
        play_game()
    elif "n" in choice:
        print_pause("Okay, thanks for playing!")
    else:
        play_again()


# Entry function.
def play_game():
    enemies = ["dragon", "fairie", "pirate"]
    enemy = random.choice(enemies)
    weapons = []
    intro(enemies)
    field(enemies, weapons)


play_game()
