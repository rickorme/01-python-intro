
#  1a)
answer = 0
for i in range(1,11):
    answer += i
print("1a) The sum of 1 to 10 is: " + str(answer))
# Svaret ska bli 55

#  1b)
answer = 0
for i in range(1,101):
    answer += i
print("1b) The sum is: " + str(answer))
# Svaret ska bli 5050

#  1b)
answer = 0
i=0
while i < 101:
    answer += i
    i += 1
print("1c) The sum is: " + str(answer))
# Svaret ska bli 5050

# 2)
print("\n2)")
answer = 0
int_list = [1, -2, 3, -2, 4, -3]
for i in int_list:
    current = answer
    answer += i
    print(f"{current} + {i} = {answer}")

print("Total of all items in the list is: " + str(answer))



