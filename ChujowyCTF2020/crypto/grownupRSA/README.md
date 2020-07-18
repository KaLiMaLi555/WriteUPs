## Grownup RSA

The challenge description says:
```
This RSA kid has grown up a bit.

Oh, the actual secret is only 31 bytes long but it was padded from the left with 97 spaces.
```


So, from the description we already know some starting bytes `(97 bytes)` of the message and the bytelength of the actual flag `(31 bytes)`. Also, after opening the txt file provided along with the description we notice `e=3`. 

I immediately thought of `Coppersmith method(https://en.wikipedia.org/wiki/Coppersmith%27s_attack)` as it states of solving of monic polynomial of degree d for all roots less than a certain value X. Honestly, I don't understand the whole math behind the attack. It was just a hunch that this could potentially solve the problem and luckily it did.

I was trying to find already written code to save some time and stumbled upon this blog (https://latticehacks.cr.yp.to/rsa.html). I wrote some more script to initialize the varibles and it worked. 

```
# k is the multiplicity of the desired roots mod N
# kd+t-1 is the degree of the polynomial that is produced
def gen_lattice(self,t=1,k=1):
	d = self.f.degree()
	dim = k*d+t
	A = matrix(IntegerRing(),dim,dim)
	x = self.R.0
	X = self.X

  monomial_list = [x^i for i in range(dim)]
	for i in range(k):
		for j in range(d):
			g = self.f(X*x)^i*(X*x)^j*self.N^(k-i)
			A[d*i+j] = [g.monomial_coefficient(mon) for mon in monomial_list]
	for j in range(t):
		g = self.f(X*x)^k*(X*x)^j
		A[k*d+j] = [g.monomial_coefficient(mon) for mon in monomial_list]

	weights = [X^i for i in range(dim)]
	def getf(M,i):
		return sum(self.R(b/w)*mon for b,mon,w in zip(M[i],monomial_list,weights))
	return A,getf

def solve(self,t=1,k=1):
	A,getf = self.gen_lattice(t,k)
	B = A.LLL(
	roots = []
	for r,multiplicity in getf(B,0).roots():
		if mod(self.f(r),self.N) == 0:
			roots.append(r)
	return roots
```

The above snippet solves a polynomial `(x+a)^d - c` using the **LLL algorithm on a lattice** to yield x hopefully. 

Running the actual script and waiting for a few second it gives the solution of the polynomial which is the flag when converted to utf-8. 

FLAG: `chCTF{D1d_y0u_us3_sm4l1_r00ts?}`
