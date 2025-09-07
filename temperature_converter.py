# Temperature Converter

print("🌡 Welcome to Temperature Converter!")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

while True:
    print("\nOptions: C = Celsius, F = Fahrenheit, K = Kelvin")
    from_unit = input("Convert from (C/F/K): ").upper()
    to_unit = input("Convert to (C/F/K): ").upper()
    value = float(input("Enter temperature value: "))

    if from_unit == "C" and to_unit == "F":
        result = celsius_to_fahrenheit(value)
    elif from_unit == "C" and to_unit == "K":
        result = celsius_to_kelvin(value)
    elif from_unit == "F" and to_unit == "C":
        result = fahrenheit_to_celsius(value)
    elif from_unit == "F" and to_unit == "K":
        result = fahrenheit_to_kelvin(value)
    elif from_unit == "K" and to_unit == "C":
        result = kelvin_to_celsius(value)
    elif from_unit == "K" and to_unit == "F":
        result = kelvin_to_fahrenheit(value)
    elif from_unit == to_unit:
        result = value
    else:
        print("❌ Invalid choice!")
        continue

    print(f"{value:.2f}{from_unit} = {result:.2f}{to_unit}")

    again = input("Do you want to convert again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break
