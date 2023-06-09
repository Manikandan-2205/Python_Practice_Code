Number_1 = int(input("Enter your Swaping number1:"))
Number_2 = int(input("Enter your Swaping number2:"))

print(f'Before Swaping your number1: {Number_1},number2: {Number_2}')

temp = Number_1
Number_1 = Number_2
Number_2 = temp

print(f'After Swaping your number1: {Number_1},number2: {Number_2}')

# -----------Anthor way of swaping ---------------

# def swap(num1,num2):
#     num2 = num1
#     num1  =num2
#     return 

# num1= int(input("Enter your Swaping number1:"))
# num2 = int(input("Enter your Swaping number2:"))

# swap(num1,num2)

# print(f'After Swaping your number1: {num2},number2: {num1}')
