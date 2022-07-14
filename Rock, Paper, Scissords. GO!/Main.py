import random





R = "Rock"
P = "Paper"
S = "Scissors"

User_Points = 0
AI_Points = 0


Best_Select = True

First_Time = False

if not Best_Select:
    First_Time = True

Best_of = 7
while True:
    # Best of Selection. Best_of is what to change if u don't want to do inputs manually.
    while Best_Select:
        Best_of = int(input("\nTo the best of what do you want to play? Enter an ODD number: "))
        if Best_of % 2 == 0:
            print(f"\nYou have entered an EVEN number. Please do it again but with an ODD number this time")
        if Best_of % 2 == 1:
            print(f"\nDo you want to play for Best of [{Best_of}]")
            Confirmation = str(input("Y = yes \nN = No\n"))
            if Confirmation == "Y" or Confirmation == "y":
                print("\nNow select which you want to do\n")
                Best_Select = False
            if Confirmation == "N" or Confirmation == "n":
                continue

    if First_Time:
        print(f"Currently playing best of {Best_of}\n")
        First_Time = False

    User_Choice = int(input("1 for Rock \n2 for Paper \n3 for Scissors \nSelect which: "))
    Ai_Choice = random.randint(1, 3)


    # All "if trees" are based on the users input


    # Rock
    if User_Choice == 1:
        print(f"\nYou have Selected {R}")
        if Ai_Choice == 1:
            print(f"Your Opponent Selected {R}")
            print(f"\nYou both Selected {R}\n")
        if Ai_Choice == 2:
            print(f"Your Opponent Selected {P}")
            print("\nYou lost and your Opponent earned 1 point")
            AI_Points = AI_Points + 1
        if Ai_Choice == 3:
            print(f"Your Opponent Selected {S}")
            print("\nYou won and earned 1 point for this")
            User_Points = User_Points + 1

    # Paper
    if User_Choice == 2:
        print(f"\nYou have Selected {P}")
        if Ai_Choice == 1:
            print(f"Your Opponent Selected {R}")
            print("\nYou won and earned 1 point for this")
            User_Points = User_Points + 1
        if Ai_Choice == 2:
            print(f"Your Opponent Selected {P}")
            print(f"\nYou both Selected {P}\n")
        if Ai_Choice == 3:
            print(f"Your Opponent Selected {S}")
            print("\nYou lost and your Opponent earned 1 point")
            AI_Points = AI_Points + 1

    # Scissors
    if User_Choice == 3:
        print(f"\nYou have Selected {S}")
        if Ai_Choice == 1:
            print(f"Your Opponent Selected {R}")
            print("\nYou lost and your Opponent earned 1 point")
            AI_Points = AI_Points + 1
        if Ai_Choice == 2:
            print(f"Your Opponent Selected {P}")
            print("\nYou won and earned 1 point for this")
            User_Points = User_Points + 1
        if Ai_Choice == 3:
            print(f"Your Opponent Selected {S}")
            print(f"\nYou both Selected {S}\n")

    if AI_Points > Best_of / 2:
        print(f"\nOpponent wins with {AI_Points} Points")
        break

    if User_Points > Best_of / 2:
        print(f"\nPlayer wins with {User_Points} Points")
        break

    print(f"\nCurrent points are {User_Points} to {AI_Points}\n")