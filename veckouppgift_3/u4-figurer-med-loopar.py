# a)
# #.......
# #.......
# #.......
# #.......
# #.......
# #.......
print("\na)")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)

# b)
# #.......
# .#......
# ..#.....
# ...#....
# ....#...
# .....#..
print("\nb)")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

# c)
# ..###...
# ..###...
# ..###...
# ..###...
# ..###...
# ..###...
print("\nc)")
for y in range(1, 7):
    s = ""
    check_list = [3,4,5]
    for x in range(1, 9):
        if x in check_list:
            s += "#"
        else:
            s += "."
    print(s)

# ..#.....
# ..#.....
# ########
# ..#.....
# ..#.....
# ..#.....
print("\nd)")
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif y == 3:
            s += "#"
        else:
            s += "."
    print(s)

# ....##..
# ....#...
# ...##...
# ..#.#...
# .#..#...
# #...#...
print("\ne)")
for y in range(1, 7):
    s = ""
    check_list = [[5, 6], [5], [4, 5], [3, 5], [2, 5], [1, 5]]
    for x in range(1, 9):
        if x in check_list[y-1]:
            s += "#"
        else:
            s += "."
    print(s)

# #....#..
# .#..#...
# ..##....
# ..##....
# .#..#...
# #....#..
print("\nf)")
for y in range(1, 7):
    s = ""
    check_list = [[1, 6], [2, 5], [3, 4], [3, 4], [2, 5], [1, 6]]
    for x in range(1, 9):
        if x in check_list[y-1]:
            s += "#"
        else:
            s += "."
    print(s)

# #.#.#.#.
# #.#.#.#.
# #.#.#.#.
# #.#.#.#.
# #.#.#.#.
# #.#.#.#.
print("\nf)")
for y in range(1, 7):
    s = ""

    for x in range(1, 9):
        if x in check_list[y-1]:
            s += "#"
        else:
            s += "."
    print(s)