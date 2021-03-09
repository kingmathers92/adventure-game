import time
import random


enemies = ["dragon", "fairie", "pirate"]
weapons = []


#Pause function. 
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


#Introduction to the game.
def intro(enemies):
    enemy = random.choice(enemies)
    print_pause("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {enemy} is somewhere "
            "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")


#The house scene.
    def house(enemies):
        if choice == '1':
            print_pause("You approach the door of the house.")
            print_pause("You are about to knock when the door opens "
                        f"and out steps a wicked {enemy}.")
            print_pause(f"Eep! This is the wicked {enemy}'s house!")
            print_pause(f"The wicked {enemy} attacks you!")
            fight = input("Would you like to (1) fight or (2) run away?")
    
            if fight == '1':
                print_pause("You do your best...")
                print_pause("but your {weapon} is no match for the troll.")
                print_pause("You have been defeated!")
            elif fight == '2':
                print_pause("You run back into the field. Luckily, you "
                            "don't seem to have been followed.")
                print_pause("You WIN!!!")
            play_again()   
            


#The cave scene. 
    def cave(enemies):
        if choice == '2':
            if "sword" in weapons:
                print_pause("You peer cautiously into the cave.")
                print_pause("It turns out to be only a very small cave.")
                print_pause("Your eye catches a glint of metal behind a rock.")
                print_pause("You have found the magical Sword of Ogoroth!")
                print_pause("You discard your silly old dagger and "
                            "take the sword with you.")
                print_pause("You walk back out to the field.")
                print_pause("He sees your magic swoard, gets scared and runs away..")
                print_pause("You WIN!!!")
                play_again()
            else:
                print_pause(f"You try to fight the {enemy} "
                            "nice try, but you weare to weak. You Lose...")
            play_again()


#The field scene.
def field(weapons):
    print_pause("You are on a crossway in the field.")
    print_pause("On your left is a house on your right "
                 "a secret cave.\n")
    print_pause("Please enter a number to make a choice.")
    choice = input("1. Go to the house\n"
                   "2. Go to the cave\n")
    if choice == "1":
        house(enemies)
    elif choice == "2":
        cave(enemies)
    else: 
        field()


#Play again feature. 
def play_again():
    choice = input("GAME OVER\n"
                   "Do you want to play again? y/n\n").lower()
    if "y" in choice:
        play_game()
    elif "n" in choice:
        print_pause("Ok, thanks for playing")


#Entry function. 
def play_game():
    enemies = ["dragon" "fairie", "pirate"]
    weapons = []  
    intro(enemies)
    field(weapons)


play_game()    
