import time
import random

beasts = ["dragon", "fairie", "pirate"]
weapons = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, "
            "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere "
            "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

while True:
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    choice = input("What would you like to do?\n"
                   "(Please enter 1 or 2).")
    def house():
        if choice == '1':
            print_pause("You approach the door of the house.")
            print_pause("You are about to knock when the door opens "
                        "and out steps a wicked fairie.")
            print_pause("Eep! This is the wicked fairie's house!")
            print_pause("The wicked fairie attacks you!")
            fight = input("Would you like to (1) fight or (2) run away?")
        def figh():
            if fight == '1':
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the troll.")
                print_pause("You have been defeated!")
            elif fight == '2':
                print_pause("You run back into the field. Luckily, you "
                            "don't seem to have been followed.")
break

        def cave():
            if choice == '2':
                print_pause("You peer cautiously into the cave.")
                print_pause("It turns out to be only a very small cave.")
                print_pause("Your eye catches a glint of metal behind a rock.")
                print_pause("You have found the magical Sword of Ogoroth!")
                print_pause("You discard your silly old dagger and "
                            "take the sword with you.")
                print_pause("You walk back out to the field.")
            else:
                print_pause("(Please enter 1 or 2.)")
