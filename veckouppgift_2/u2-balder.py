"""
To ride Balder at Liseberg you must be 130 cm tall. Write a program that can tell if you are allowed to ride!

Ask the user how tall they are (in cm)
Print either "You may ride!" or "You may not ride"

Test Cases:
 - 121 cm (not allowed to ride)
 - 130 cm (allowed to ride)
 - 155 cm (allowed to ride)
"""
allowed_to_ride = False
minimum_rider_height = 130
rider_height = int(input("Enter your height in cm: "))

if rider_height >= minimum_rider_height:
    allowed_to_ride = True

print(f"Your rider height is {rider_height}cm...")
print(f"The minimum rider height is {minimum_rider_height}cm...")

if allowed_to_ride:
    print("You may ride! 🎢🤘")
else:
    print("You may not ride 😭")




