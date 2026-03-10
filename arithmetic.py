#all usefull airthmetic function for classic RSA
import random
def exp_modulo(a,exp,q):
    res = 1
    a = a % q
    while exp > 0:
        if exp % 2 == 1:
            res = (res * a) % q
        exp = exp // 2
        a = (a * a) % q
    return res

    #take two prime number and return phi(p*q)=phi(p)*phi(q)=(p-1)*(q-1)
def euler(p,q):
    return (p-1)*(q-1)
    
def extended_pgcd(a,b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_pgcd(b % a, a)
        return g, x - (b // a) * y, y

    

def is_prime_with(e,phi_N):
    return extended_pgcd(e,phi_N)[0]==1

def inverse_modulo(e,phi_N):
    g, x, y = extended_pgcd(e, phi_N)
    return x%phi_N

#we use miller rabin test and we use k =40 it's opti
def is_prime(n,k=40):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = exp_modulo(a, d, n) 
        if x == 1 or x == n - 1:
                continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(nbits=1024):
    while True:
        p = random.getrandbits(nbits)
        p |= (1 << nbits - 1) | 1 
        if is_prime(p):
            return p