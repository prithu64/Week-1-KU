def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius = float(input("Enter the celsius temp : "))
result = celsius_to_fahrenheit(celsius)

print(f"{celsius} celsius in Fahrenheit is {result}")