
import sympy

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

cislo = int(input("číslo: "))


def jednodusi_prvocislo(num):
    return sympy.isprime(num)