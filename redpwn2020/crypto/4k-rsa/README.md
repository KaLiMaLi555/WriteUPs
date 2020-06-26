**4k-rsa**

Computed factors of n using alpertron.
Then its just a simple multi-prime RSA decryption


```
phi = 1

for p in factors:
	phi *= (int(p) - 1)


d = inverse(int(e), phi)

plain = pow(int(ct), d, int(n))

print('Flag =', long_to_bytes(plain).decode())
```

FLAG: `flag{t0000_m4nyyyy_pr1m355555}`