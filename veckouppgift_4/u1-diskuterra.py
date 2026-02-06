from main import print_exercise_divider
# 1 Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
#
# 1a
# This will print "test"
print_exercise_divider("1a")

def foo(t):
    print("test")

foo("hej")

# 1b
#  This will print "3 5"
print_exercise_divider("1b")

def fun1(x, y):
    return x * y

print(3, 5)

# 1c
# This will print 15
print_exercise_divider("1c")

def fun1(x, y):
    return x * y

print(fun1(3, 5))

# 1d
# This will print 125

print_exercise_divider("1d")

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y)) # 5 * ( (5 * 2) + (5 * 3) ) = 5 * (10 + 15) = 5 * 25 = 125
print(a)

# 1e
# This will print 7

print_exercise_divider("1e")

a = 5
def fun3(a):
    a += 1

a += 2
print(a)

# 1f
# This will print 18
# the function foo is passed as a parameter - not immediately run
print_exercise_divider("1f")

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y) # here 'x' is a reference to the function foo, i.e. it is going to run foo(y) or foo(3)

a = goo(foo, 3);
print(a)


# 1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
# is_number returns True if x is either an int or a float, otherwise it returns False
# It can be improved by passing a tuple with both datatypes we want to check
# so that the check is completed in a single line
print_exercise_divider("1g")

def is_number(x):
    if isinstance(x, (int, float)):
        return True
    # if isinstance(x, int):
    #     return True
    # elif isinstance(x, float):
    #     return True
    return False

print(is_number(5.5))
print(is_number(42))
print(is_number("12"))

# 1h
# Should return ["how's", "going", "coding"]
print_exercise_divider("1h")

def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

# average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
found_words = average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
print(found_words)


# 1i En uppgift i tre delar:
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
# Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
# Rätta felen, så funktionen gör det den ska.
print_exercise_divider("1i")
# the purpose of the function is to accept a list of numbers, and return the smallest
# run 1 -> -11
# run 2 -> error
# run 3 -> 0

# def find_min(numbers):
#     counter = 0
#     for item in numbers:
#         if item < counter:
#             counter = item
#     print(f"The smallest item is: {counter}")
#     return counter
def find_min(numbers):
    counter = 0
    min_num = 0
    if len(numbers) == 0:
        print("No numbers provided")
    else:

        for item in numbers:
            if counter == 0:
                min_num = item
            elif item < min_num:
                min_num = item
            counter += 1
        print(f"The smallest item is: {min_num}")

    return min_num

find_min([10, 3, -4, -11])
find_min([])
find_min([100])