import random
import time

Values = []
Time_Values = []
# Select1 = int(input("How many times do you want it to do? "))
# Select1 is for the amount completions
Select1 = int(input("How many Significant figures do you want? Maximum is 9: "))
Select2 = int(input("How many iterations do you want it to complete: "))

SF = Select1
Select1 = 10**Select1


Total_Tries = 0
# to just print out a message
y = 0
x = 1
Time_Data = True
R_Number = True
Data = True
Start = time.time()
while Data:
    y = y + 1
    if y > (Select1/5):
        x = x + 1
        y = 0
        if x % 2 == 1:
            print("Calculating...")
        else:
            print("...Calculating")

    # Just the randomizer, and selection of Value to chose
    if Data:
        Number = random.randint(1, 1_000_000)

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
        R_Number = False

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
        if len(Values) > Select1:
            End = time.time()
            # for i in Values:
            #     print(i)
            # print("\n\n")
            Values.sort()
            # for I in Values:
            #     print(i)
            # print(f"Fastest was {Values[0]}")
            # print(f"Longest was {Values[-1]}")
            # print(f"Total tries was {Total_Tries}")
            Time = End - Start
            Time = round(Time, 10)
            Time_Values.append(Time)
            # print(f"It took {Time}")
            Active = False

    if len(Time_Values)+1 > Select2:
        Total_End = time.time()
        print("\n\n")
        Time_Values.sort()
        # for i in Time_Values:
        #     print(i)
        print(f"Fastest was {Time_Values[0]}")
        print(f"Longest was {Time_Values[-1]}")

        print(f"Average time was {sum(Time_Values) / len(Time_Values)}")
        print(f"The amount of digits was {SF}")
        print(f"The amount of iterations was {Select2}")
        Total_Time = Total_End - Start
        Total_Time = round(Total_Time, 10)
        print(f"The total time it took was: {Total_Time}")
        Time_Data = False
        Data = False
