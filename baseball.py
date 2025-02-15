import random
import os

os.system("title Baseball")

def get_input():
    while True:
        try:
            num = int(input("Choose a number --> 1 or 2: "))
        except KeyboardInterrupt:
            print("\n-- Program stopped --")
            exit()
        except ValueError:
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
        usr_choice = input("Enter heads or tails: ").strip().upper()
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
    
    usr_bat = toss()
    usr_score = 0
    c_score = 0
    innings = 0
    target = 0

    print("\nYou are BATTING\n" if usr_bat else "\nYou are PITCHING\n")
    
    while True:
        c_run = random.randint(1, 2)
        usr_run = get_input()
        print(f"Computer's choice: {c_run}")

        if usr_run != c_run:
            if usr_bat:
                usr_score += 1
                print(f"Your score: {usr_score}")
            else:
                c_score += 1
                print(f"Computer's score: {c_score}")
        else:
            print("<< OUT >>")
            innings += 1
            
            if innings == 2:
                break

            print(f"\nYour Final Score: {usr_score}" if usr_bat else f"\nComputer's Final Score: {c_score}")
            target = usr_score + 1 if usr_bat else c_score + 1
            print(f"\nTarget: {target}")
            usr_bat = not usr_bat
            print("\nYou are BATTING\n" if usr_bat else "\nYou are PITCHING\n")
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
