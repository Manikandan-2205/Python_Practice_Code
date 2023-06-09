import math

number = int(input("Enter Number:"))

print(f'your factorial number is: {math.factorial(number)}')

print("**********Anthor way of factorial pogram************")

factorial = 1

if number < 0:
    print("We can't find factorial in nagative number")
elif (number == 0 or number == 1):
    print("The number of 0 and 1 is same value")
else:
    for i in range(1, number+1):
        factorial = factorial * i
    print(f"The factorial of", number, 'is', factorial)

print("**********Anthor way of factorial pogram************")


def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n-1)


print(f"The factorial of", number, 'is', factorial(number))
