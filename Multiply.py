def multiply(x, y):

    if(y == 0):
        return 0

    if(y > 0):
        return (x+multiply(x, y-1))

    if(y < 0):
        return -multiply(x, -y)


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(num1, "X", num2, "=", multiply(num1, num2))
