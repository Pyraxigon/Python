import random
import time

Values = []
Select = int(input("How many times do you want it to do? "))

Start = time.time()

Total_Tries = 0
# to just print out a message
y = 0
Data = True
while Data:
    y = y + 1
    if y > 400:
        print("Calculating")
        y = 0
    # Just the randomizer, and selection of Value to chose
    if Data:
        Number = random.randint(1, 1_000_000_000)

        # Exact number
        Correct = Number

        # to use for top value
        Top_Digits = len(str(Number))

        # To know how high the
        Digits = len(str(Number))
        Digits = -int(Digits)
        Digits = Digits + 1

        # High End
        Top_Value = (10 ** Top_Digits) - 1

        Min = 1
        Top_Value = Top_Value
        Guess = random.randint(Min, Top_Value)

    x = 0
    # The Bot Guesser
    Active = True
    while Active:
        x = x + 1
        Guess = random.randint(Min, Top_Value)

        if Guess < Correct:
            Min = Guess
            Top_Value = Top_Value

        if Guess > Correct:
            Min = Guess / 2
            round(Min, 0)
            Min = int(Min)
            Top_Value = Guess

        if Guess == Correct:
            Correct = str(Correct)
            Values.append(["Tries: ", x, "Correct Value", Correct, (len(Correct) - 1), "zeros"])
            Active = False
            Total_Tries = Total_Tries + x
            y = y + 1

        if x > 10000:
            Values.append(["Tries Too many", x])
            continue

    # Length of tries, and time1
    if len(Values) > Select:
        End = time.time()
        for i in Values:
            print(i)
        print("\n\n")
        Values.sort()
        for i in Values:
            print(i)
        print(f"Fastest was {Values[0]}")
        print(f"Longest was {Values[-1]}")
        print(f"Total tries was {Total_Tries}")
        Time = End - Start
        Time = round(Time, 3)
        print(f"It took {Time}")
        break