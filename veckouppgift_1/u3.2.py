jacket_price = 2000
discount_percent = float(input("Please enter the discount as a percentage: "))

discount_amount = jacket_price * (discount_percent / 100)
final_price = jacket_price - discount_amount

print("Original price is: " + str(jacket_price))
print("Discount is " + str(discount_percent) + "% (" + str(discount_amount) + " kronor)")
print("Amount to pay is: " + str(final_price) + " kronor")
