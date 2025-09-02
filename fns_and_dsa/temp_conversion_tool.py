from os import system
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temp = 0.0


def convert_to_celsius():
    global temp
    temp = (temperature * FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit():
    global temp
    temp = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR)

while True:
    temperature = input("Enter the temperature to convert: ")
    choice = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).upper()
    if not temperature.isdigit():
        print("Invalid temperature. Please enter a numeric value.")
        system('cls')
        continue
    if choice == 'C' :
        temperature = float(temperature)
        convert_to_fahrenheit()
        print(f"{temperature}°C is {temp}°F")
    elif choice == 'F' :
        temperature = float(temperature)
        convert_to_celsius()
        print(f"{temperature}°F is {temp}°C")
    
