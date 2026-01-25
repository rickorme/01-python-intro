is_member = False
level1 = 100
level2 = 300
discount = 0


price = input("Välkommen, köp något dyrt: ")
price = float(price)

"""
because there are 2 separate if statements, both will run, 
resulting in a discount of 35% instead of 25%
"""
if price > level1:
    print("Grattis! Du hara avancerat till nivå 1 och får 10% rabatt.")
    discount = discount + 10

if price >= level2:
    print("Grattis! Du hara avancerat till nivå 2 och får 25% rabatt.")
    discount = discount + 25

final_price = price * (100 - discount) / 100
print("\n")
print("-"*50)
print(f"Originalpris är {price} kr, rabatten är {discount}% ")
print(f"Efter rabatter blir priset...{final_price} kr")