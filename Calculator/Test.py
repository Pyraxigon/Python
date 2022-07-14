# This is my calculator Script


import math

# Remains of an idea I had before.

# Selection = (input("\nSelect one of those listed: "))
#
# if Selection == isinstance(Selection, float):
#    Selection = 5
#    pass
# elif Selection != isinstance(Selection, float):
#    Selection = float(Selection)


# Want to do a 'short memory
# Project for later


# Total Below is referred to with "Short Memory"
# globals()
#   Total = Total + Value_One
#   Value_One = Value_Two
#   Value_Two = Input_Value
#   Test for In puts

List_of_Options = "Enter one of the following letters for its corresponding \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division\n5 For Parentheses (Soon to be added)\n6 for Resetting it \n9 For Advanced"

List_of_Options_Brackets = "Enter one of the following letters for its corresponding \n1 I want to ADD this value to total \n2 I want to SUBTRACT this value from total \n3 I want to MULTIPLY this value from the total \n4 I want to DIVIDE this value from the total \n5 To finish Bracket Mode and Calculate \n6 I want to go back to start with the previous Total \n9 For Advanced"

List_of_Options_in = "Enter one of the following letters for its corresponding \n1 for Addition \n2 for Subtraction \n3 for Multiplication \n4 for Division \n5 To finish Bracket Mode and Calculate \n6 I want to go back to start with the previous Total"
# To The power of, Circumference, Area, Volume (simple), Pythagorean Theorem, square root of.
List_of_Options_Advanced = "Enter one of the following letters for its corresponding \n1 for Exponents \n2 for Square root \n3 for Circumference \n4 for Areas \n5 for Volumes \n6 for Pythagorean Theorem \n7 to Exit"


print(List_of_Options)

#    Selection = input("Select One of the Following: ")
#    Input_Value = float(input("Enter A Number: "))
Total = 0
Bracket_Value = 0
# First_Time = True

Counter = 0
Counter_Brackets = 0
Advanced_Counter = 0
First_Bracket = True
Bracket_Selection = True
First_Advanced = True
while True:
    # Skip Is for Multiplication and Division Keep it
    Counter = Counter + 1
    skip = False
    First_Bracket = True
    Bracket_Selection = True
    if Counter > 3:
        print(List_of_Options)
        Counter = 1
    if Total > 0 or Total < 0:
        print(f"\nCurrent Total is {Total}")
    Selection = int(input("\nSelect one of those listed: "))
    if Selection < 5:
        Input_Value = float(input("Enter A Number: "))

    # Addition
    if Selection == 1:
        print("\nADDITION SELECTED")
        print(f"  {Total}\n+ {Input_Value} \n{ + len(str(Total + 3)) * '-' + (6 * '-')}")
        Total = Total + float(Input_Value)
        print(f"  {Total}")


    # Subtraction
    if Selection == 2:
        print("\nSUBTRACTION SELECTED")
        print(f"  {Total}\n- {Input_Value} \n{+ len(str(Total + 3)) * '-' + (6 * '-')}")
        Total = Total - float(Input_Value)
        print(f"  {Total}")


    # Multiplication
    if Selection == 3:
        if Total > 0 or Total < 0:
            print("\nMULTIPLICATION SELECTED")
            print(f"  {Total}\nx {Input_Value} \n{ + len(str(Total + 3)) * '-' + (6 * '-')}")
            Total = Total * float(Input_Value)
            print(f"  {Total}")
        if Total == 0:
            print("\nYou need to have a number before trying to multiply")


    # Division
    if Selection == 4:
        if Total != 0:
            if Input_Value == 0:
                skip = True
                print("Cant Divide by zero")
                continue
            if skip == False:
                print("\nDIVISION SELECTED")
                print(f"  {Total}\n/ {Input_Value} \n{+ len(str(Total + 3)) * '-' + (6 * '-')}")
                Total = Total / float(Input_Value)
                print(f"  {Total}")
        if Total == 0:
            print("\nYou need to have a number before trying to divide")


    # Brackets
    if Selection == 5:
        print("\nParentheses Selected\n")
        Brackets = True
        while Brackets == True:
            Counter_Brackets = Counter_Brackets + 1
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
                if Counter_Brackets > 3:
                    print(f"\n{List_of_Options_in}")
                    Counter_Brackets  = 1
            Selection = int(input("\nSelect What you want to happen: "))
            # if 1 == 1
            if Selection > 5:
                print(f"\nYou tried selecting something that is outside of the range")
                pass
            if Selection < 4:
                Input_Value = float(input("Enter A Number: "))

        # Addition
            if Selection == 1:
                print("\nADDITION SELECTED")
                Bracket_Value = Bracket_Value + float(Input_Value)

        # Subtraction
            if Selection == 2:
                print("\nSUBTRACTION SELECTED")
                Bracket_Value = Bracket_Value - float(Input_Value)

        # Multiplication
            if Selection == 3:
                if Bracket_Value != 0:
                    print("\nMULTIPLICATION SELECTED")
                    Bracket_Value = Bracket_Value * float(Input_Value)
                if Bracket_Value == 0 and Selection == 4:
                    print("\nYou need to have a number before trying to multiply")
                    pass

        # Division
            if Selection == 4:
                if Total != 0:
                    if Input_Value == 0:
                        skip = True
                        print("Cant Divide by zero")
                        continue
                    if skip == False:
                        print("\nDIVISION SELECTED")
                        Total = Total / float(Input_Value)

            if Selection == 5:
                Brackets = False
                if Bracket_Choice == 1:
                    # Addition
                    Total = Total + Bracket_Value
                if Bracket_Choice == 2:
                    # Subtraction
                    Total = Total - Bracket_Value
                if Bracket_Choice == 3:
                    # Multiplication
                    Total = Total * Bracket_Value
                if Bracket_Choice == 4:
                    # Division
                    Total = Total / Bracket_Value
            if Selection == 6:
                break

        # Clear
        if Selection == 6:
            Total = 0
            print(f"Your Total has been reset and now is {Total}")


        # Advanced Subsystem
        # To The power of, Circumference, Area, Volume (simple), Pythagorean Theorem
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
                print(f"\nEXPONENTS SELECTED")
                Base = float(input("Enter The Base: "))
                Exponent = float(input("Enter The Exponent: "))
                Output = Base ** Exponent
                print(f"The total with a Base of {Base} and exponent {Exponent} is {Output}")

            # Square root of
            if Selection == 2:
                print(f"\nSQUARE ROOT SELECTED")
                Base = float(input("Enter the Base: "))
                Root = math.sqrt(Base)
                Root_Round = round(Root, 3)
                print(f"The Square root of {Base} is {Root_Round}")

            # Circumference
            if Selection == 3:
                print(f"\nCIRCUMFERENCE SELECTED")
                print(f"1 for Circle \n2 for Rectangle \n3 for Square")
                Selection = int(input("\nSelect one of those listed: "))


                if Selection == 1:
                    print("\nCIRCLE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Circle_Circumference = Radius * 2 * math.pi
                    Circle_Circumference_Round = round(Circle_Circumference, 3)
                    print(Circle_Circumference_Round)
                    print(f"Circumference of a Circle with Radius {Radius} is {Circle_Circumference_Round}")

                if Selection == 2:
                    print("\nRECTANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Rectangle_Circumference = Base*2 + Height*2
                    Rectangle_Circumference_Round = round(Rectangle_Circumference, 3)
                    print(f"Circumference of a Rectangle with Base {Base} and Height {Height} is {Rectangle_Circumference_Round}")

                if Selection == 3:
                    print("\nSQUARE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Square_Circumference = Base*4
                    Square_Circumference_Round = round(Square_Circumference, 3)
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
                    Circle_Area_Round = round(Circle_Area, 3)
                    print(f"\nArea of a Circle with Radius {Radius} is {Circle_Area_Round}")

                if Selection == 2:
                    print("CYLINDER SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cylinder_Area = 2 * ((math.pi * Radius * Height) + (math.pi * Radius ** 2))
                    Cylinder_Area_Round = round(Cylinder_Area, 3)
                    print(f"\nArea of a Cylinder with Radius {Radius} and Height {Height} is {Cylinder_Area_Round}")

                if Selection == 3:
                    print("\nSPHERE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Sphere_Area = 4 * (Radius ** 2) * math.pi
                    Sphere_Area_Round = round(Sphere_Area, 3)
                    print(f"\nArea of a Sphere with Radius {Radius} is {Sphere_Area_Round}")

                if Selection == 4:
                    print("\nRECTANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Rectangle_Area = Base*Height
                    Rectangle_Area_Round = round(Rectangle_Area, 3)
                    print(f"\nArea of a Rectangle with Base {Base} and Height {Height} is {Rectangle_Area_Round}")

                if Selection == 5:
                    print("\nSQUARE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Square_Area = Base ** 2
                    Square_Area_Round = round(Square_Area, 3)
                    print(f"\nArea of a Square with Base {Base} is {Square_Area_Round}")

                if Selection == 6:
                    print("\nTRIANGLE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Height = float(input("Enter The Height: "))
                    Triangle_Area = (Base * Height) / 2
                    Triangle_Area_Round = round(Triangle_Area, 3)
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
                    Sphere_Volume_Round = round(Sphere_Volume, 3)
                    print(f"\nVolume of a Sphere with Radius {Radius} is {Sphere_Volume_Round}")

                if Selection == 2:
                    print("\nCone SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cylinder_Volume = (Radius ** 2) * math.pi * Height
                    Cylinder_Volume_Round = round(Cylinder_Volume, 3)
                    print(f"\nVolume of a Cylinder with Radius {Radius} and Height {Height} is {Cylinder_Volume_Round}")

                if Selection == 3:
                    print("CONE SELECTED")
                    Radius = float(input("Enter The Radius: "))
                    Height = float(input("Enter The Radius: "))
                    Cone_Volume = (Radius ** 2) * math.pi * (Height / 3)
                    Cone_Volume_Round = round(Cone_Volume, 3)
                    print(f"\nVolume of a Cone with Radius {Radius} and Height {Height} is {Cone_Volume_Round}")

                if Selection == 4:
                    print("CUBOID SELECTED")
                    Base = float(input("Enter The Base: "))
                    Width = float(input("Enter The Width: "))
                    Height = float(input("Enter The Height: "))
                    Cuboid_Volume = Base*Height*Width
                    Cuboid_Volume_Round = round(Cuboid_Volume, 3)
                    print(f"\nVolume of a Cuboid with Base {Base}, Height {Height} and Width {Width} is {Cuboid_Volume_Round}")

                if Selection == 5:
                    print("\nCUBE SELECTED")
                    Base = float(input("Enter The Base: "))
                    Cube_Volume = Base ** 3
                    Cube_Volume_Round = round(Cube_Volume, 3)
                    print(f"\nVolume of a Cube with Base {Base} is {Cube_Volume_Round}")

                if Selection == 6:
                    print("\nPYRAMID SELECTED")
                    Base = float(input("Enter The Base: "))
                    Width = float(input("Enter The Width: "))
                    Height = float(input("Enter The Height: "))
                    Pyramid_Volume = (Base * Height * Width) / 3
                    Pyramid_Volume_Round = round(Pyramid_Volume, 3)
                    print(f"\nVolume of a Pyramid with Base {Base}, Height {Height} and Width {Width} is {Pyramid_Volume_Round}")

            # Pythagorean theorem
            if Selection == 6:
                print(f"PYTHAGOREAN THEOREM")
                A_Leg = float(input("Enter The Base: "))
                B_leg = float(input("Enter The Base: "))
                Hypotenuse = math.sqrt((A_Leg ** 2) + (B_leg ** 2))
                Hypotenuse_Round = round(Hypotenuse, 3)
                print(f"The Hypotenuse of a Right Angled Triangle With side {A_Leg} and side {B_leg} is {Hypotenuse_Round}")

            # Break
            if Selection == 7:
                print(f"EXIT")
    elif Selection > 6 and Selection < 8:
        print(f"\nERROR \n\nWhat You Have Entered Does Not Match any Command. Try Again Please.\n\n")
        if Advanced_Counter != 3:
            print(List_of_Options)

