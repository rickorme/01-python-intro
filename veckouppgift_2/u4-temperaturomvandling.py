"""
Write a program that can convert a temperature in degrees Celsius to degrees Fahrenheit.
Version 1, example output:

Enter a temperature in degrees Celsius: 22
This gives 71.6 degrees Fahrenheit.

Version 2: first ask the user if they want to enter the temperature in Celsius or Fahrenheit.
Then the program converts to the other temperature.
Tip: ask the user to enter e.g. "F" if they want to enter the temperature in Fahrenheit. Then use if + else.

Version 3: if the temperature being converted is below 10°C, the program should also tell the user to put on winter clothes.
And if the temperature is at least 20°C, it should suggest that they pack swimwear.

Formula for converting between temperature units:
C = (F - 32) / 1.8
F = 1.8 * C + 32

Suggested values to test with:

°Celsius |  °Fahrenheit
------------------------
0        |   32
-17.777… |   0
37.777…  |   100
100      |   212
"""
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

print("🌡️🌡️ Welcome to the temperature converter 🌡️🌡️")
print("-----------------------------------------------\n")

f_or_c = input("Do you want to enter a temperature in Fahrenheit (type F) or Celsius (type C)?: ")
temperature = float(input("Enter the temperature to convert: "))
print("\n")

if f_or_c.upper() == "F":
    degrees_fahrenheit = temperature
    degrees_celsius = fahrenheit_to_celsius(degrees_fahrenheit)
    print(f"{degrees_fahrenheit} °F equals {degrees_celsius}°C")

elif f_or_c.upper() == "C":
    degrees_celsius = temperature
    degrees_fahrenheit = celsius_to_fahrenheit(degrees_celsius)
    print(f"{degrees_celsius} °C equals {degrees_fahrenheit}°F")
else:
    print("Invalid input. Try again.")
    exit(1)



if degrees_celsius < 10:
    advice = "It's cold, put on your winter clothes!"
elif degrees_celsius >= 20:
    advice = "It's warm, pack your swimmers! 🌞"
else:
    advice = ""

if len(advice) > 0:
    print(advice)





