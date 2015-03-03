def modpow2(base, exponent, exponent2, mod):
    c = 1
    for i in range(0, exponent*exponent2):
        c = (c * base) % mod
    return c

input1 = int(input("Enter base: "))
input2 = int(input("Enter exponent: "))
input3 = int(input("Enter exponent's exponent: "))
input4 = int(input("Enter mod: "))
print("modpow = ", modpow2(input1, input2, input3, input4))