# Halloween themed Adventure Game
import time
def intro():
    print("Welcome to the Haunted House Adventure!")
    player_name = input("What's your character's name? ")
    print(f"You, {player_name}, find yourself in front of a spooky mansion on Halloween night.")
    print("Your goal is to explore the mansion and survive the night.")
    print("Be careful of your choices, and good luck!\n")

def choose_path():
    while True:
        choice = input("You stand in front of two doors. Will you enter the 'Left' door or the 'Right' door? ").strip().lower()
        if choice == "left":
            left_door()
            break
        elif choice == "right":
            right_door()
            break
        else:
            print("Invalid choice. Please enter 'Left' or 'Right'.")

def left_door():
    print("\nYou enter the left door and find a dark hallway.")
    print("At the end of the hallway, you see three more doors.")
    time.sleep(1)
    print("As you approach, you hear faint whispers.")
    while True:
        choice = input("Will you choose the 'Red' door, the 'Blue' door, or the 'Green' door? ").strip().lower()
        if choice == "red":
            print(f"You opened the Red door and found a room full of spooky ghosts.")
            print("You are now haunted forever. Game over.")
            break
        elif choice == "blue":
            print(f"You opened the blue door and found a room with a talking skeleton.")
            print("The skeleton offers you a riddle. Solve it to proceed.")
            skeleton_riddle()
            break
        elif choice == "green":
            print(f"You opened the green door and found a room with a friendly witch.")
            print("The witch offers you a magical potion. Drink it or decline?")
            witch_potion()
            break
        else:
            print("Invalid choice. Please enter 'Red', 'Blue', or 'Green'.")

def right_door():
    print("\nYou enter the right door and find a creepy laboratory.")
    print("In the corner, there's a potion bottle with three choices.")
    while True:
        choice = input("Will you drink the 'Red' potion, the 'Blue' potion, or the 'Green' potion? ").strip().lower()
        if choice == "red":
            print(f"The red potion was poisonous. You are now a ghost forever. Game over!")
            break
        elif choice == "blue":
            print(f"The blue potion turned you into a zombie forever. Game over.")
            break
        elif choice == "green":
            print(f"The green potion was a healing elixir. You are safe!")
            print(f"Congratulations! You survived the night!")
            break
        else:
            print("Invalid choice. Please enter 'Red', 'Blue', or 'Green'.")

def skeleton_riddle():
    print("The skeleton presents the riddle:")
    print("I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person.")
    while True:
        answer = input("What am I? ").strip().lower()
        if answer == "pencil":
            print(f"Correct! The skeleton has granted you his blessings and you win!")
            break
        else:
            print(f"Wrong! The skeleton disappears, and you are lost in the mansion. Game over.")

def witch_potion():
    while True:
        choice = input("Will you 'Drink' the potion or 'Decline'? ").strip().lower()
        if choice == "drink":
            print(f"You drank the potion. It's a magical potion that makes you invisible.")
            print("You can now explore the mansion safely. Keep going!")
            continue_exploring()
            break
        elif choice == "decline":
            print(f"You declined the witch's potion. She wishes you good luck and you continue exploring.")
            continue_exploring()
            break
        else:
            print("Invalid choice. Please enter 'Drink' or 'Decline'.")

def continue_exploring():
    print("You find yourself in a hallway with three more doors.")
    while True:
        choice = input("There are 'Gold' door, 'Silver' door, and 'Bronze' door. Choose Gold, Silver, or Bronze: ").strip().lower()
        if choice == "gold":
            print(f"You opened the Gold door and found a room filled with treasures!")
            print("Congratulations, you won!")
            break
        elif choice == "silver":
            print(f"You opened the Silver door and encountered a mischievous ghost.")
            print("The ghost tricks you into a never-ending loop. Game over!")
            break
        elif choice == "bronze":
            print(f"You opened the Bronze door and found an exit!")
            print("You've successfully escaped the haunted mansion. You win!")
            break
        else:
            print("Invalid choice. Please enter 'Gold', 'Silver', or 'Bronze'.")

def play_game():
    while True:
        intro()
        choose_path()
        play_again = input("Would you like to play again? (yes/no) ").strip().lower()
        if play_again != "yes":
            break

# Main loop
play_game()
