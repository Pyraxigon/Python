# This is Pyraxigons calculator Script with extras.


import math


List_of_Options = "Enter one of the following letters for its corresponding \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division\n5 for Parentheses \n6 for Resetting it \n7 to  view History \n9 for Advanced \n0 for Settings"

List_of_Options_Brackets = "Enter one of the following letters for its corresponding \n1 I want to ADD this value to total \n2 I want to SUBTRACT this value from total \n3 I want to MULTIPLY this value from the total \n4 I want to DIVIDE this value from the total \n5 To finish Bracket Mode and Calculate \n6 I want to go back to start with the previous Total"

List_of_Options_in = "Enter one of the following letters for its corresponding \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n5 To finish Bracket Mode and Calculate \n6 I want to go back to start with the previous Total"

List_of_Options_Advanced = "Enter one of the following letters for its corresponding \n1 for Exponents \n2 for Square root \n3 for Circumference \n4 for Areas \n5 for Volumes \n6 for Pythagorean Theorem \n7 to Exit"

List_of_Settings = "Which of the following settings would u like to edit \n1 History Length \n2 Decimal points \n7 to Exit Settings"

print(List_of_Options)


Total = 0
Bracket_Value = 0

Counter = 0
Brackets_Counter = 0
Advanced_Counter = 0
Settings_Counter = 0
Eight_Counter = 0

First_Bracket = True
Bracket_Selection = True
First_Advanced = True
Settings = False

History = [[0]]
History_Length = 10

Decimal_places = 3

while True:
    # Skip Is for Multiplication and Division Keep it
    Counter = Counter + 1
    First_Bracket = True
    Bracket_Selection = True
    skip = False
    Settings = False
    Brackets = False

    # When to print Options
    if Counter > 3:
        print(List_of_Options)
        Counter = 1

    # If to print Total
    if Total != 0:
        print(f"\nCurrent Total is {Total}")
        pass

    # Just input.
    if 1 == 1:
        Selection = int(input("\nSelect one of those listed: "))
        pass

    # History Clearer
    while len(History) >= History_Length:
        History.pop(0)
        pass

    # To Check if it needs float input or notat
    if 0 < Selection < 5:
        print("")
        Input_Value = float(input("Enter A Number: "))


    # 1 Addition
    if Selection == 1:
        Symbol = "+"
        print("\nADDITION SELECTED")
        print(f"  {Total}\n+ {Input_Value} \n{ + len(str(Total + 3)) * '-' + (6 * '-')}")
        Total = Total + float(Input_Value)
        print(f"  {Total}")
        History.append([Input_Value, Symbol, Total])
        Eight_Counter = 0


    # 2 Subtraction
    if Selection == 2:
        Symbol = "-"
        print("\nSUBTRACTION SELECTED")
        print(f"  {Total}\n- {Input_Value} \n{+ len(str(Total + 3)) * '-' + (6 * '-')}")
        Total = Total - float(Input_Value)
        print(f"  {Total}")
        History.append([Input_Value, Symbol, Total])
        Eight_Counter = 0


    # 3 Multiplication
    if Selection == 3:
        if Total > 0 or Total < 0:
            Symbol = "*"
            print("\nMULTIPLICATION SELECTED")
            print(f"  {Total}\nx {Input_Value} \n{ + len(str(Total + 3)) * '-' + (6 * '-')}")
            Total = Total * float(Input_Value)
            print(f"  {Total}")
            History.append([Input_Value, Symbol, Total])
            Eight_Counter = 0
        if Total == 0:
            print("\nYou need to have a number before trying to multiply")
            Eight_Counter = 0


    # 4 Division
    if Selection == 4:
        if Total != 0:
            if Input_Value == 0:
                skip = True
                print("Cant Divide by zero")
                continue
            if skip == False:
                Symbol = "/"
                print("\nDIVISION SELECTED")
                print(f"  {Total}\n/ {Input_Value} \n{+ len(str(Total + 3)) * '-' + (6 * '-')}")
                Total = Total / float(Input_Value)
                print(f"  {Total}")
                History.append([Input_Value, Symbol, Total])
                Eight_Counter = 0
        if Total == 0:
            print("\nYou need to have a number before trying to divide")
            Eight_Counter = 0


    # 5 Brackets
    if Selection == 5:
        Eight_Counter = 0
        print("\nParentheses Selected\n")
        Brackets = True
        while Brackets:
            Brackets_Counter = Brackets_Counter + 1
            print(f"\nTotal outside of brackets: {Total}")
            print(f"Total inside of Brackets: {Bracket_Value}")
            if Bracket_Selection == True:
                print(List_of_Options_Brackets)
                Selection = int(input("\nSelect what you want to happen to this Bracket: "))
                Bracket_Selection = False
                if Selection > 6:
                    break
                Bracket_Choice = Selection
            if First_Bracket == True:
                print(List_of_Options_in)
                First_Bracket = False
            if Bracket_Selection == False:
                if Brackets_Counter > 3:
                    print(f"\n{List_of_Options_in}")
                    Brackets_Counter  = 1
            Selection = int(input("\nSelect What you want to happen: "))
            # if 1 == 1
            if Selection > 5:
                print(f"\nYou tried selecting something that is outside of the range")
                pass
            if Selection < 5:
                Input_Value = float(input("Enter A Number: "))

            # Addition Brackets
            if Selection == 1:
                Symbol = "+"
                print("\nADDITION SELECTED")
                Bracket_Value = Bracket_Value + float(Input_Value)
                History.append(["()", Input_Value, Symbol, Bracket_Value])

            # Subtraction Brackets
            if Selection == 2:
                Symbol = "-"
                print("\nSUBTRACTION SELECTED")
                Bracket_Value = Bracket_Value - float(Input_Value)
                History.append(["()", Input_Value, Symbol, Bracket_Value])

            # Multiplication Brackets
            if Selection == 3:
                if Bracket_Value != 0:
                    Symbol = "*"
                    print("\nMULTIPLICATION SELECTED")
                    Bracket_Value = Bracket_Value * float(Input_Value)
                    History.append(["()", Input_Value, Symbol, Bracket_Value])
                if Bracket_Value == 0 and Selection == 4:
                    print("\nYou need to have a number before trying to multiply")
                    pass

            # Division Brackets
            if Selection == 4:
                if Total != 0:
                    if Input_Value == 0:
                        skip = True
                        print("Cant Divide by zero")
                        continue
                    if skip == False:
                        Symbol = "/"
                        print("\nDIVISION SELECTED")
                        Bracket_Value = Bracket_Value / float(Input_Value)
                        History.append(["()", Input_Value, Symbol, Bracket_Value])

            # Bracket "Action"
            if Selection == 5:
                Brackets = False
                if Bracket_Choice == 1:
                    # Addition
                    Symbol = "+"
                    Total = Total + Bracket_Value
                    History.append(["()", Bracket_Value, Symbol,  Total])
                if Bracket_Choice == 2:
                    # Subtraction
                    Symbol = "-"
                    Total = Total - Bracket_Value
                    History.append(["()", Bracket_Value, Symbol,  Total])
                if Bracket_Choice == 3:
                    # Multiplication
                    Symbol = "*"
                    Total = Total * Bracket_Value
                    History.append(["()", Bracket_Value, Symbol,  Total])
                if Bracket_Choice == 4:
                    # Division
                    Symbol = "/"
                    Total = Total / Bracket_Value
                    History.append(["()", Bracket_Value, Symbol,  Total])
            if Selection == 6:
                print(f"Back to Main")
                break


    # 6 Clear
    if Selection == 6:
        Total = 0
        print(f"Your Total has been reset and now is {Total}")
        Eight_Counter = 0


    # 7 History Viewer
    if Selection == 7:
        for i in History:
            print(i)
            Counter = Counter - 1
            Eight_Counter = 0


    # 8 Advanced Subsystem
    if Selection == 9:
        print(f"\nADVANCED SELECTED")
        Advanced = True
        while Advanced:
            Advanced_Counter = Advanced_Counter + 1
            if First_Advanced == True:
                print(List_of_Options_Advanced)
                First_Advanced = False
            if Advanced_Counter > 3:
                print(List_of_Options_Advanced)
                Advanced_Counter = 1
            Selection = int(input("\nSelect one of those listed: "))

            # To the power of
            if Selection == 1:
                Output = 0
                Symbol = "^"
                print(f"\nEXPONENTS SELECTED")
                Base = float(input("Enter The Base: "))
                Exponent = float(input("Enter The Exponent: "))
                Output = Base ** Exponent
                print(f"The total with a Base of {Base} and exponent {Exponent} is {Output}")
                History.append([Base, Symbol, Exponent, "  ", Output])

            # Square root of
            if Selection == 2:
                Symbol = "Sqrt()"
                print(f"\nSQUARE ROOT SELECTED")
                Base = float(input("Enter the Base: "))
                Root = math.sqrt(Base)
                Root_Round = round(Root, Decimal_places)
                print(f"The Square root of {Base} is {Root_Round}")
                History.append([Symbol, Base, "  ", Output])

            # Circumference
            if Selection == 3:
                print(f"\nCIRCUMFERENCE SELECTED")
                print(f"1 for Circle \n2 for Rectangle \n3 for Square")
                Selection = int(input("\nSelect one of those listed: "))


                if Selection == 1:
                    print("\nCIRCLE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Circle_Circumference = Radius * 2 * math.pi
                    Circle_Circumference_Round = round(Circle_Circumference, Decimal_places)
                    print(Circle_Circumference_Round)
                    print(f"Circumference of a Circle with Radius {Radius} is {Circle_Circumference_Round}")

                if Selection == 2:
                    print("\nRECTANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Rectangle_Circumference = Base*2 + Height*2
                    Rectangle_Circumference_Round = round(Rectangle_Circumference, Decimal_places)
                    print(f"Circumference of a Rectangle with Base {Base} and Height {Height} is {Rectangle_Circumference_Round}")

                if Selection == 3:
                    print("\nSQUARE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Square_Circumference = Base*4
                    Square_Circumference_Round = round(Square_Circumference, Decimal_places)
                    print(f"Circumference of a Square with Base {Base} is {Square_Circumference_Round}")

            # Area
            if Selection == 4:
                print(f"\nAREA SELECTED")
                print(f"1 for Circle \n2 for Cone \n4 for Rectangle \n5 for Square \n6 For Triangle")
                Selection = int(input("\nSelect one of those listed: "))

                if Selection == 1:
                    print("\nCIRCLE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Circle_Area = (Radius ** 2) * math.pi
                    Circle_Area_Round = round(Circle_Area, Decimal_places)
                    print(f"\nArea of a Circle with Radius {Radius} is {Circle_Area_Round}")

                if Selection == 2:
                    print("CYLINDER SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cylinder_Area = 2 * ((math.pi * Radius * Height) + (math.pi * Radius ** 2))
                    Cylinder_Area_Round = round(Cylinder_Area, Decimal_places)
                    print(f"\nArea of a Cylinder with Radius {Radius} and Height {Height} is {Cylinder_Area_Round}")

                if Selection == 3:
                    print("\nSPHERE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Sphere_Area = 4 * (Radius ** 2) * math.pi
                    Sphere_Area_Round = round(Sphere_Area, Decimal_places)
                    print(f"\nArea of a Sphere with Radius {Radius} is {Sphere_Area_Round}")

                if Selection == 4:
                    print("\nRECTANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Rectangle_Area = Base*Height
                    Rectangle_Area_Round = round(Rectangle_Area, Decimal_places)
                    print(f"\nArea of a Rectangle with Base {Base} and Height {Height} is {Rectangle_Area_Round}")

                if Selection == 5:
                    print("\nSQUARE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Square_Area = Base ** 2
                    Square_Area_Round = round(Square_Area, Decimal_places)
                    print(f"\nArea of a Square with Base {Base} is {Square_Area_Round}")

                if Selection == 6:
                    print("\nTRIANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Triangle_Area = (Base * Height) / 2
                    Triangle_Area_Round = round(Triangle_Area, Decimal_places)
                    print(f"\nArea of a Triangle with Base {Base} and Height {Height} is {Triangle_Area_Round}")

            # volume
            if Selection == 5:
                print(f"VOLUME SELECTED")
                print(f"1 for Sphere \n2 for Cylinder \n3 for Cone \n4 for Cuboid \n5 for Cube \n6 For Pyramid")
                Selection = int(input("\nSelect one of those listed: "))

                if Selection == 1:
                    print("\nSPHERE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Sphere_Volume = 4/3 * (Radius ** 3) * math.pi
                    Sphere_Volume_Round = round(Sphere_Volume, Decimal_places)
                    print(f"\nVolume of a Sphere with Radius {Radius} is {Sphere_Volume_Round}")

                if Selection == 2:
                    print("\nCone SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cylinder_Volume = (Radius ** 2) * math.pi * Height
                    Cylinder_Volume_Round = round(Cylinder_Volume, Decimal_places)
                    print(f"\nVolume of a Cylinder with Radius {Radius} and Height {Height} is {Cylinder_Volume_Round}")

                if Selection == 3:
                    print("CONE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cone_Volume = (Radius ** 2) * math.pi * (Height / 3)
                    Cone_Volume_Round = round(Cone_Volume, Decimal_places)
                    print(f"\nVolume of a Cone with Radius {Radius} and Height {Height} is {Cone_Volume_Round}")

                if Selection == 4:
                    print("CUBOID SELECTED")
                    Base = float(input("Enter The Base: "))
                    Width = float(input("Enter The Width: "))
                    Height = float(input("Enter The Height: "))
                    Cuboid_Volume = Base*Height*Width
                    Cuboid_Volume_Round = round(Cuboid_Volume, Decimal_places)
                    print(f"\nVolume of a Cuboid with Base {Base}, Height {Height} and Width {Width} is {Cuboid_Volume_Round}")

                if Selection == 5:
                    print("\nCUBE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Cube_Volume = Base ** 3
                    Cube_Volume_Round = round(Cube_Volume, Decimal_places)
                    print(f"\nVolume of a Cube with Base {Base} is {Cube_Volume_Round}")

                if Selection == 6:
                    print("\nPYRAMID SELECTED")
                    Base = float(input("Enter The Base: "))
                    Width = float(input("Enter The Width: "))
                    Height = float(input("Enter The Height: "))
                    Pyramid_Volume = (Base * Height * Width) / 3
                    Pyramid_Volume_Round = round(Pyramid_Volume, Decimal_places)
                    print(f"\nVolume of a Pyramid with Base {Base}, Height {Height} and Width {Width} is {Pyramid_Volume_Round}")

            # Pythagorean theorem
            if Selection == 6:
                print(f"PYTHAGOREAN THEOREM")
                A_Leg = float(input("Enter The Base: "))
                B_leg = float(input("Enter The Base: "))
                Hypotenuse = math.sqrt((A_Leg ** 2) + (B_leg ** 2))
                Hypotenuse_Round = round(Hypotenuse, Decimal_places)
                print(f"The Hypotenuse of a Right Angled Triangle With side {A_Leg} and side {B_leg} is {Hypotenuse_Round}")

            # Break
            if Selection == 7:
                print(f"Back to Main")
                print(List_of_Options)
                break


    # 9 Nothing/error, + Meme
    if Selection == 8:
        Eight_Counter = Eight_Counter + 1
        if Eight_Counter == 1:
            print(f"Invalid input. Try again")
        if Eight_Counter == 2:
            print("\nWhy you click it again. There is nothing to see here.")
        if Eight_Counter == 3:
            print("\nStop it already")
        if Eight_Counter == 4:
            print("\nYou dont know how to listen to instructions? \nI told you to stop already.")
        if Eight_Counter == 5:
            print("\nDo it one more time. \nI \nDARE \nYOU.")
        if Eight_Counter == 6:
            print("I told you")
            break


    # 0 Settings
    if Selection == 0:
        print(List_of_Settings)
        print(f"\nSETTINGS SELECTED")
        Settings = True
        while Settings:
            Settings_Counter = Settings_Counter + 1
            if Settings_Counter > 3:
                print(List_of_Settings)

            print(f"In SETTINGS")
            Selection = int(input("\nSelect one of those listed: "))

            # History Length
            if Selection == 1:
                print(f"\nCurrent History Length is: {History_Length}")
                Change = str(input(f"\nDo you want to change the History Length? \nY or N\n"))
                # Check input and yes and no
                if Change.isalpha():
                    if Change == "Y" or "y":
                        Length = input(f"\nWhat length of the History do you want: ")
                        History_Length = Length
                        print(f"History Length is now {History_Length}")
                    if Change == "N" or "n":
                        print(f"\nEXITING HISTORY LENGTH OPTION")
                        pass
                if not Change.isalpha:
                    print(f"\nError")
                    pass

            # Decimal places
            if Selection == 2:
                print(f"\nCurrent Amount of Decimal Places is {Decimal_places}")
                # Check input and yes and no
                Change = str(input(f"\nDo you want to change the number of decimal places? \nY or N\n"))
                if Change.isalpha and Change == "Y" or "y":
                    Length = input(f"\nWhat amount of decimal places do do you want: ")
                    Decimal_places = Length
                    print(f"Decimal palces now displayed is {Decimal_places}")
                if Change.isalpha and Change == "N" or "n":
                    print(f"\nEXITING DECIMAL PLACES OPTION")
                pass
                if not Change.isalpa:
                    print(f"\nError")
                pass


            if Selection == 7:
                print(f"Back to Main")
                print(List_of_Options)
                break


    # >9 Else
    if Selection > 9:
        print("\nYou have entered value outside the range. Please try again.")
        pass
