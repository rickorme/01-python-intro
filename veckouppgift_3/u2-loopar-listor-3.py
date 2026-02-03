def print_list_length():
    print(f"List length is {len(film_list)}\n")

film_fellowship = "Fellowship of the ring"
film_2towers = "The two towers"
film_platoon = "Platoon"

# a)
film_list = ["Old Boy","Deadwood",film_platoon,"Winter in Sokcho"]
print_list_length()
print(film_list)
# b)
print(f"Add film {film_fellowship}")
film_list.append(film_fellowship)
position = film_list.index(film_fellowship)
print(position)
print_list_length()
# c)
print(f"Add filem {film_2towers}")
film_list.insert(0,"The two towers")
print_list_length()
# d)
position = film_list.index('Fellowship of the ring')
print(f"{film_fellowship} position is {position}")
print_list_length()
# e)
print(f"Removing film {film_platoon}")
film_list.remove("Platoon")
position = film_list.index('Fellowship of the ring')
print(f"{film_fellowship} position is {position}")
# f)
print_list_length()
# g)
print(f"Film list in reverse")
film_list.reverse()
print(film_list)
# h)
print(f"Film list in alphabetical order")
film_list.sort()
print(film_list)




mixed_list = [1,"3",19,"2"]
print(mixed_list)
# mixed_list.sort() - gives an error
mixed_list = [int(x) for x in mixed_list]
print(mixed_list)
mixed_list.sort()
print(mixed_list)