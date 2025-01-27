def Even_or_Odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num=float(input("Enter the number : "))

result = Even_or_Odd(num)

print(f"The number {num} is {result} ")