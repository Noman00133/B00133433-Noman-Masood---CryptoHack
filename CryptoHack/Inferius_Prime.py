from Crypto.Util.number import long_to_bytes

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

# factordb.com to get the prime factorization and the values of p and q
p = 752708788837165590355094155871
q = 986369682585281993933185289261

# Euler's totient function
PHI = (p-1)*(q-1)

# inverse of e modulo PHI
d = pow(e, -1, PHI)

#Decrypt the ciphertext using the private key (d) and the modulus (n)
flag = long_to_bytes(pow(ct, d, n))
print(flag)



