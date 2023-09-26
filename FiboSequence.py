def fiboSequence():
    n = int(input("Enter the amount of numbers in the sequence: "))

    num1 = 0
    num2 = 1
    for i in range(n):
        print(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2


def getNthFiboNum():
    n = int(input("Enter a number to find in the Fibonacci sequence: "))

    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        print('Your number is: {}'.format(a))
    elif n == 1:
        print('Your number is: {}'.format(b))
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        print('Number {} in the sequence is: {}'.format(n,b))

fiboSequence()
getNthFiboNum()