def lcm(x, y):
    return (x*y)/gcd(x, y)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

input1 = int(input("Enter number: "))
input2 = int(input("Enter second number: "))
print("The least common multiple of", input1, " and ", input2, " is ", lcm(input1, input2))