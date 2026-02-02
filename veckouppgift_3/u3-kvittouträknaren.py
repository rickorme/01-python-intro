user_input = ""
input_list = []
number_of_people = 0
total_amount = 0
tip_amount = 0
total_with_tip = 0
tip_percentage = 0
standard_tip_percentage = "10"
amount_per_person = 0

print("💶"*50)
print("\nWelcome to the cost calculator\n")

# Build the list of amounts from user input, quite on 'q', gracefully handle bad input
while user_input != "q":
    user_input = input("Please enter an amount in kronor (or 'q' to quit): ")

    if user_input != "q":
        try:
            input_list.append(float(user_input))
        except:
            print(f"Invalid input ({user_input}) 😩, try again...")

# Now get the number of people, only accept integers
continue_program = False
while not continue_program:
    number_of_people = input("How many people are there?: ")
    if number_of_people.isdigit():
        number_of_people = int(number_of_people)

        if number_of_people > 0:
            # All input requirements satisfied
            continue_program = True

    if not continue_program:
        # Not all input requirements satisfied
        print(f"Invalid number of people ({number_of_people})! Please enter a whole number ...")

# Now calculate the total amount
for i in input_list:
    total_amount += i

print(f"\n{len(input_list)} amounts input, totalling {round(total_amount,2)} kronor")

# Check if the user wants to add a tip
continue_program = False
while not continue_program:
    tip_percentage = input(f"Please enter a tip percentage, or press 'Enter' to accept the standard {standard_tip_percentage}%: ") or standard_tip_percentage

    if tip_percentage.isdigit():
        tip_percentage = int(tip_percentage)
        if tip_percentage >= 0:
            # All input requirements satisfied
            continue_program = True
    else:
        # Not all input requirements satisfied
        print(f"Invalid input ({tip_percentage})! Please enter a positive whole number...")


# Calculate the total + tip
tip_amount = total_amount * (tip_percentage/100)
total_amount = total_amount + tip_amount

print(f"\nIncluding a tip of {tip_amount:.2f}, the new total is {total_amount:.2f} kronor")

# Calculate the amount per person
amount_per_person = total_amount / number_of_people

print(f"Each person pays {amount_per_person:.2f} kronor")
