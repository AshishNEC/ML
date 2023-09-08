"""Function to check whether triangle"""


def is_triangle(side1, side2, side3):
    if side1 > (side2 + side3) or side2 > (side1 + side3) or side3 > (side1 + side2):
        return 'No'
    return 'Yes'


# 5.3.1
# print("Is Triangle possible: ", is_triangle(5,10, 2))


# 5.3.2
side1 = int(input("Enter side1 value:"))
side2 = int(input("Enter side2 value:"))
side3 = int(input("Enter side3 value:"))

print("Is Triangle possible with given user values: ", is_triangle(side1, side2, side3))
