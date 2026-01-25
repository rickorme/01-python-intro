"""
1 Write a program that asks the user for 3 numbers. Then it should calculate the sum, and print it on the console. (sum: number1 + number2 + number3)

2 The program should tell you which is the largest number, without using the Python function max. Instead, use if/elif/else. Think about whether you can solve the problem in different ways.

3 The program should tell you if two of the numbers are equal, or all three are equal.

4 The program should tell you which is the middle number. Note that there is only one middle number if all three are different,
  or all three are equal. (If the numbers were, for example, 2, 2, 5, none of them would count as the middle number in this problem.)

To test systematically, you can make a table. Then run the program.
Check that the program prints the same things that you have entered into the table. We call the numbers t1, t2 and t3.
Suggested values to test with: 1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16
"""
def build_phrase(bool_check: bool, true_phrase: str, false_phrase: str):
    if bool_check:
        return true_phrase
    else:
        return false_phrase


t1 = int(input("Please enter the first number: "))
t2 = int(input("Please enter the second number: "))
t3 = int(input("Please enter the third number: "))

equal_count = 0
middle_number = 0
three_equal = False
look_for_middle_number = True
found_greatest_number = False
t1_is_greatest = False
t2_is_greatest = False
t3_is_greatest = False

# If all three numbers equal we know the max and the middle
if t1 == t2 == t3:
    three_equal = True
    equal_count = 3
    greatest_number = t1
    middle_number = t1
    found_greatest_number = True

# If 2 numbers are equal, there is no middle number, but we still need to find the max
elif (t1 == t2) or (t1 == t3) or (t2 == t3):
    look_for_middle_number = False
    equal_count = 2


if not found_greatest_number:

    # check if t1 is greatest
    if t1 > (t2 + t3) /2:
        greatest_number = t1
        t1_is_greatest = True
    # check if t2 is greatest
    elif t2 > (t1 + t3)/2:
        greatest_number = t2
        t2_is_greatest = True
    # t3 must be greatest
    else:
        greatest_number = t3
        t3_is_greatest = True


if look_for_middle_number and not three_equal:

    if t1_is_greatest:
        if t2 > t3:
            middle_number = t2
        else:
            middle_number = t3
    elif t2_is_greatest:
        if t1 > t3:
            middle_number = t1
        else:
            middle_number = t3
    elif t3_is_greatest:
        if t1 > t2:
            middle_number = t1
        else:
            middle_number = t2


result_msg = f"\nThe 3 numbers entered are {t1}, {t2} and {t3}."

result_msg += f"\n{equal_count} numbers are equal."

result_msg += build_phrase(look_for_middle_number, f"\nThe middle number is {middle_number}", "\nThere is no middle number")

result_msg += f"\nThe greatest number is {greatest_number}."

print(result_msg)


