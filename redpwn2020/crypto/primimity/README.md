**primimity**

The custom prime prime generator uses a seed to generate the next prime
The prime generated should be very close to the seed.

```
def find_next_prime(n):
    if n <= 1:
        return 2
    elif n == 2:
        return 3
    else:
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        while not isPrime(n):
            n += 2
        return n
```

So, I computed the cube root of the modulus provided and run a loop to find the values of the primes used

```
qroot = gmpy2.iroot(n, 3)[0]

for i in range(qroot, qroot+20000000):
	if is_prime(i):
		if n % i == 0:
			print(i)
```
This gives us p, q, r

The rest is simple RSA decryption
```
phi = 1

for p in factors:
	phi *= (int(p) - 1)


d = inverse(int(e), phi)

plain = pow(int(ct), d, int(n))

print('Flag =', long_to_bytes(plain).decode())
```