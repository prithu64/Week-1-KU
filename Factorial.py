def factorial(num):
    if num == 0 : 
        return 1
    return num* factorial(num-1)

num = float(input("Enter the number : "))

result = factorial(num)

print(f"The factorial of the number {num} is {result}")