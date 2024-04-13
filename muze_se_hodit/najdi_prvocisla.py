import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

for i in range(int(input("prvni: ")), int(input("druhe: "))):
    if is_prime(i):
        print(i ,end=", ")


input("konec")