#python calculator
""""
operator =input("enter an operator (+ - * /): ")
num1= float(input("enter first number: "))
num2 = float(input("enter second number: "))

if operator== "+":
    result = num1 + num2
    print(result)
elif operator== "-":
    result = num1 - num2
    print(result)
elif operator== "*":
    result = num1 * num2
    print(round(result))
elif operator== "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print("Pick valid operator from the following : +, -, *, /")

#weight conversion

weight= float(input("enter your weight: "))
unit= input("Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lb"
    print(f"{round(weight, 2)}{unit}")
elif unit == "L":
    weight= weight / 2.205
    unit = "Kg"
    print(f"{round(weight, 2)}{unit}")
else:
    print(f"The {unit} entered is invalid")
"""
# Temperature

unit = input("Is the temperature Celsius or Fahrenheit (C/F): ")
temperature = float(input("enter your temperature: "))

if unit == "C":
    temperature = round(temperature * 9 / 5 + 32, 2)
    unit = "Fahrenheit"
    print(f"The temperature is {temperature} {unit}")
elif unit == "F":
    temperature = round(temperature * 9 / 5 - 32, 2)
    unit = "Celsius"
    print(f"The temperature is {temperature} {unit}")
else:
    print(f"The {unit} entered is invalid")