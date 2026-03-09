from encryptor import *
import random

chn="je veux savoir"

chn_int=Encryptor.string_to_int(chn)

print("le message chiffré :",chn_int)
p=arithmetic.generate_prime()
q=arithmetic.generate_prime()
n=p*q
phi_N=arithmetic.euler(p,q)
e= 65537
while(arithmetic.is_prime_with(e,phi_N)!=True):
    e= random.randint(2, phi_N-1)

d=arithmetic.inverse_modulo(e,phi_N)

r=arithmetic.exp_modulo(chn_int,e,n)

print("message crypté:",r)
dec=arithmetic.exp_modulo(r,d,n)
print("message décrypté:",dec)
final_msg = Encryptor.int_to_string(dec)
print(final_msg)