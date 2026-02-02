limit = 15
index = 5

# 1) the following code will print:
# 5
# 7
# 9
# 11
# 13
# 15
while index <= limit:
    print(index)
    index = index + 2

exercise = 1
print("\n","-"*40,"\n")
print(f"exercise {exercise}")
exercise += 1


# 2) the following code will print:
# 0
# 1
# 2
# 3
# 4
#
# 6
# 7
# 8
# 9
for i in range(10):
    if i ==5:
        print("")
    else:
        print(i)
    i = i + 1


print("\n","-"*40,"\n")
print(f"exercise {exercise}")
exercise += 1


# 3) the sum will be 6
counter = 0
for i in range(6):
    counter += 1
print(counter)


print("\n","-"*40,"\n")
print(f"exercise {exercise}")
exercise += 1


# 4)
# y=1, x=0+1    = 1
# y=2, x=1-2    = -1
# y=3, x=-1+9   = 8
# y=4, x=8-4    = 4
# y=5, x=4+25   = 29
# y=6, x=29-6   = 23
# y=7, x=23+49  = 72
# y=8, x=72-8   = 64
# y=9, x=64+81  = 145
x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1
    print(x)


print("\n","-"*40,"\n")
print(f"exercise {exercise}")
exercise += 1


# 5)
message ="its_time_to_get_coding"
print(message[3:7]) # -> "_tim"
print(message[4:8]) # -> "time"


print("\n","-"*40,"\n")
print(f"exercise {exercise}")
exercise += 1

# loop  12345678 (line number
# 1      #.......
# 2      .#......
# 3      ..#.....
# 4      ...#....
# etc
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)





