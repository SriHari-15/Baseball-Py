import random
import os

os.system("title Baseball")

def get_input():
    while True:
        try:
            num = int(input("Choose a number --> 1 or 2: "))
        except KeyboardInterrupt: # Without this, you wont be able to stop the program when pressing CTRL + C
            print("\n-- Program stopped --")
            exit()
        except ValueError: # Prevents the program from closing when an input error occurs
            print("ERROR | Enter a valid number")
            continue
        
        if num in (1, 2):
            return num
        else:
            print("ERROR | Please choose either 1 or 2")

# To simplify, we'll be considering user batting as True and user pitching as False

def toss():
    print("-- TOSS --")
    while True:
        usr_choice = input("Enter heads or tails: ").strip().upper() # Removes any spaces and converts to uppercase
        if usr_choice not in ("HEADS", "TAILS"):
            print("ERROR | Please enter 'Heads' or 'Tails'")
            continue
        break

    if usr_choice == random.choice(["HEADS", "TAILS"]):
        print("You won the TOSS!")
        while True:
            choice = input("Choose one - bat or pitch: ").strip().upper()
            if choice in ("BAT", "BATTING"):
                return True
            elif choice in ("PITCH", "PITCHING"):
                return False
            else:
                print("ERROR | Please enter 'bat' or 'pitch'")
    else:
        print("You lost the TOSS :(")
        return bool(random.randint(0, 1)) # Thanks ChatGPT :)

def game():
    print("--- BASEBALL ---\n")
    print("> How to Play?")
    print("- Toss will be held and you will choose either batting or pitching")
    print("- If both players enter the same number, then the batting player gets 1 run")
    print("- If they enter a different number, the batting player gets 1 Strike")
    print("- When the batting player accumulates 3 consecutive Strikes, they are declared OUT and one innings is over")
    print("- At the end of first innings, the final score of the batting player along with the target will be displayed")
    print("- Now the pitching player will be batting and the same rule applies")
    print("- If the batting player in the 2nd innings reaches the target, they WIN")
    print("- If they get 3 Strikes and are OUT, they LOSE\n")
    
    # Variables initialization
    usr_bat = toss()
    usr_score = 0
    c_score = 0
    innings = 0
    target = 0

    print("\nYou are BATTING\n" if usr_bat else "\nYou are PITCHING\n")
    
    counter = 1 # Strikes counter
    
    while True:
        c_run = random.randint(1, 2)
        usr_run = get_input()
        print(f"Computer's choice: {c_run}")

        if usr_run == c_run:
            counter = 1
            if usr_bat:
                usr_score += 1
                print(f"\n> Your score: {usr_score}\n")
            else:
                c_score += 1
                print(f"\n> Computer's score: {c_score}\n")
        else:
            if counter == 3: # This statement is triggered only on 3 consecutive strikes
                print(f"\n>> STRIKE: 3")
                print("\n<< OUT >>")
                innings += 1
            else: # Increments the strike counter when there aren't 3 consecutive strikees
                print(f"\n>> STRIKE: {counter}\n")
                counter += 1
                continue # To prevent the program from executing the bottom messages | They are reserved only for first innings ending
            
            if innings == 2:
                break

            # Would be better to put this in an if statement? if innings == 1 | Would improve readability, not sure
            print(f"\nYour Final Score: {usr_score}" if usr_bat else f"\nComputer's Final Score: {c_score}")
            target = usr_score + 1 if usr_bat else c_score + 1
            print(f">> TARGET: {target}")
            usr_bat = not usr_bat
            print("\nYou are BATTING\n" if usr_bat else "\nYou are PITCHING\n")
            counter = 1 # To reset the counter after first innings
            continue

        if innings == 1 and ((usr_bat and usr_score >= target) or (not usr_bat and c_score >= target)): # Thanks ChatGPT :)
            break

    print("\n-- FINAL SCORES --")
    print(f"Your Score: {usr_score}")
    print(f"Computer's Score: {c_score}\n")
    if usr_score > c_score:
        print(">> YOU WIN! <<")
    elif c_score > usr_score:
        print(">> YOU LOSE! <<")
    else:
        print(">> DRAW <<")

game()
input("\nPress ENTER to exit")
