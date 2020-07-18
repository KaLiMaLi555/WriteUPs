# Baby RSA

For this challenge we are given a chall.py which shows that the flag was encrypted two times with two different public key pairs

Keys: `N1, e)` and `(N2, e)`

```
c1 = flag^e (modN1)
ct = c1^e (modN2)
```

Using factordb we find the prime factors of N1 and N2. At that point the challenge seems to finished as now we can find the private keys `d1` and `d2` and decrypted the provided ciphertext. But it turns out that `gcd(e, phi(N2)) = e` which implies that the private exponent d2 does not exist. 

I was googling for some time to find a solution for this problem. Then, I remembered that I can just take the **eth root** of the ciphertext. The problem of finding the eth root of a number `C modulo N` is just as hard as **factoring N**. And as we have the prime factors of N2 available finding all the eth roots of the given `ct` is very easy.

I used sagemath for this as there is an already implemented routine for finding all eth root there.
```
ct = mod(ct, N2)

## Calculating all eth roots of ct in sagemath
roots = ct.nth_root(e, all=True)

## As N1 < N2, we know c1 < N1
c1 = [i for i in roots if i < N1][0]
```

We first find all the eth roots of ct and find for the values of `ct^(1/e)` that are less than N1 (As c1 is encrypted modulo N1). 
And there is only one such value among the roots.

Now, the only that is remaining is to find the flag by decrypting c1. I tried doing this normally by finding d1 and I don't know why this didn't work. So, I again just used the routine for `finding eth root and filtered by considering the flag will be the smallest among all`.
```
## Calculating all eth roots of c1 in sagemath
roots = c1.nth_root(e, all=True)

## Checking for flag < sqrt(N1)
m = [i for i in roots if i < sqrt(N1)][0]

print(long_to_bytes(m))
```

And, we find the flag!!!

FLAG: `chCTF{finally_an_RSA_challenge_I_can_solve}`
