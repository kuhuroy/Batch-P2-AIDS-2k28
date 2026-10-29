#3.WAP to find if the number prime.
import math

def is_prime(n):
    if n<2:
        return False

    for i in range(2, math.isqurt(n)+1):
        if n % i ==0:
            return False

        return True

n = int(input("enter a munber : "))
print("prime" if is_prime(n) else "not prime")    
