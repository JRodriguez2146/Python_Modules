def fiboSequence():
    n = int(input("Enter a number."))

    num1 = 0
    num2 = 1
    for i in range(n):
        print(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2



fiboSequence()