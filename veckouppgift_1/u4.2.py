import math

print("Welcome to the Hypotenuse calculator!")

len_a = input("Enter the length of side A: ")
len_a = float(len_a)
len_b = input("Enter the length of side B: ")
len_b = float(len_b)

len_h = math.sqrt(len_a ** 2 + len_b ** 2)

print("When side A is: " + str(len_a) + " long")
print("And side B is: " + str(len_b) + " long...")
print("The hypotenuse is: " + str(len_h) + " long")

print("Credits: Pythagoras")