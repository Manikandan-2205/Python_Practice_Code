try:

    def prim_number():
        num = int(input("Enter your number:"))

        if num < 2:
            print(f"{num} is not a prime number")

        else:
            for i in range(2, num):
                if num % i == 0:
                    print(f"{num} is not a prime number")
                    break
            else:
                print(f'{num} is a prime number')

except Exception as e:
    print(e)
else:
    prim_number()

finally:
    print("This Numbe is identified")


print('****************************************')


start = int(input("Enter your starting range:"))
end = int(input("Enter your ending range:"))

print(f'{start} to {end} prime numbers:')

for i in range(start, end+1):
    flag = 0
    for j in range(2, i):
        if (i % j == 0):
            flag = 1
            break
    if (flag == 0):
        print(i, end=' ')
