import random

def getinput():
    while 0<1:
        try:
            num = int(input("Choose a number --> 1 or 2: "))
        except KeyboardInterrupt:
            print("-- Program stopped --")
            break
        except:
            print("ERROR | Enter a valid number")
            continue
        
        if num == 1 or num == 2:
            return num
        else:
            print("ERROR | Please choose a number between 1 or 2")
            continue

# To simplify, we'll be considering that user batting as True and user pitching as False

def toss():
    print("-- TOSS --")
    while 0<1:
        usr_choice = input("Enter heads or tails: ").upper()
        if usr_choice != "HEADS" and usr_choice != "TAILS":
            print("ERROR | Please enter a valid choice --> Heads or Tails")
            continue
        break
    c_choice = ["HEADS", "TAILS"]
    if usr_choice == c_choice[random.randint(0,1)]:
        print("You won the TOSS!")
        while 0<1:
            choice = input("Choose one - bat or pitch: ").upper()
            if choice != "BAT" and choice != "BATTING" and choice != "PITCH" and choice != "PITCHING":
                print("ERROR | Please enter a valid choice --> bat, batting, pitch or pitching")
                continue
            break
        if choice == "BAT" or choice == "BATTING":
            return True
        else:
            return False
    else:
        print("You lost the TOSS :(")
        choice = random.randint(0,1)
        if choice == 0: # COnsidering 0 means batting
            return False
        else:
            return True
        
def game():
    print("--- BASEBALL ---")
    print()
    
    usr_bat = toss()
    usr_score = 0
    c_score = 0
    innings = 0
    target = 0

    print("\nYou are BATTING\n" if usr_bat else "\nYou are PITCHING\n")
    
    while 0 < 1:
        c_run = random.randint(1,2)
        usr_run = getinput()
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

        if innings == 1 and ((usr_bat and usr_score >= target) or (not usr_bat and c_score >= target)):
            break

    if usr_score > c_score:
        print("\n>> YOU WIN! <<")
    elif c_score < usr_score:
        print("\n>> YOU LOSE! <<")
    else:
        print("\n>> DRAW <<")

game()
