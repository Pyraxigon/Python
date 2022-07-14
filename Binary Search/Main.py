import random

# A copy paste from my previous random number finder project
# I tried to do 1_000_000_000 but it froze my computer for a few seconds so i keep it at MAX at 100_000_000
item_a = random.randint(1, 100_000_000)

Top_Digits = len(str(item_a))

# To know how high the
Digits = len(str(item_a))
Digits = -int(Digits)
Digits = Digits + 1

# High End
Top_Value = (10 ** Top_Digits)

# Just to make sure range is large. Can replace "Top_Value" inside "Range" to any value to select a specific size.
Range = range(1, Top_Value)
Options = list(Range)
Options.sort

# Just the basic values for them. the globals*
lower = 0
x = 0
upper = Top_Value
middle = (upper + lower) // 2
correct_value = Options[middle]

Times_List = []

x = 0
while lower <= upper:
    x += 1
    print(middle)

    # For Completion
    if middle == item_a:
        Times_List.append(["It took", x, "tries for Value: ", item_a])
        print(Times_List)
        break


    # if the midpoint is too high and need to move it lower
    if middle > item_a:
        lower = lower
        upper = middle
        middle = (lower + upper) // 2

    # if the midpoint is too low and need to move it higher
    if middle < item_a:
        lower = middle
        upper = upper
        middle = (lower + upper) // 2
