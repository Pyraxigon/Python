import math


First_Advanced = True
List_of_Options_Advanced = ("aa")
List_of_Options_Ain = ("bb")
Advanced_Counter = 1

#if Selection == 9:
#    print(f"ADVANCED SELECTED")
#    Advanced = True
#    while Advanced:
#        Advanced_Counter = Advanced_Counter + 1
#        if First_Advanced == True:
#            print(List_of_Options_Advanced)
#            First_Advanced = False
#        if Advanced_Counter > 3:
#            print(List_of_Options_Ain)
#            Advanced_Counter = 1
#        Selection = int(input("\nSelect one of those listed: "))
#

# print(f"SQUARE ROOT SELECTED")
# Base = float(input("Enter Number you want to take the root out of: "))
# # Exponent = int(input("Enter The Radical value: "))
# Output = Base ** 0.5
#
# print(Output)

#Base = float(input("Enter Number you want to take the root out of: "))

# print("CIRCLE SELECTED")
# Radius = float(input("Enter The Radius: "))
# Circle_Circumference = Radius * 2 * math.pi
# Circle_Circumference_Round = round(Circle_Circumference, 3)
# print(Circle_Circumference_Round)


#print("SPHERE SELECTED")
#Radius = float(input("Enter The Radius: "))
#Sphere_Volume = 4 / 3 * (Radius ** 3) * math.pi
#
#print(Sphere_Volume)


#Radius = 7
#Height = 9
#Cylinder_Area = 2 * ((math.pi * Radius * Height) + (math.pi * Radius ** 2))
#print(round(Cylinder_Area))

#   print(f"PYTHAGOREAN THEOREM")
#   A_Leg = float(input("Enter The Base: "))
#   B_leg = float(input("Enter The Base: "))
#   Hypotenuse = math.sqrt((A_Leg ** 2) + (B_leg ** 2))
#   Hypotenuse_Round = round(Hypotenuse, 3)

def Float_Check(input):
    try:
        Input = int(Selection)
        print(f"Input is an Integer Number. The number is {Input}")
    except ValueError:
        try:
            Input = float(Selection)
            print(f"Input is a float number. The number is {Input}")
        except ValueError:
            print("Input is a string")

Selection = 2.3
Float_Check(Selection)

Selection = "2.3"
Float_Check(Selection)

Selection = "2q"
Float_Check(Selection)
