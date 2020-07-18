from Crypto.Util.number import *

## Coppersmith class
class univariate_coppersmith:
	# degree d polynomial f
	# integer modulus N
	# X is the bound on the absolute value of the root
	def __init__(self, f, N, X):
		self.f = f
		self.N = N
		self.X = X
		self.R = QQ['x']

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
		B = A.LLL()
		roots = []
		for r,multiplicity in getf(B,0).roots():
			if mod(self.f(r),self.N) == 0:
				roots.append(r)
		return roots

# can solve up to rlen < nlen/d
def gen_random_coppersmith(nlen=1024, rlen=150, d=3):
	p = random_prime(2^floor(nlen/2),False)
	q = random_prime(2^ceil(nlen/2),False)
	N = p*q
	a = ZZ.random_element(0,2^(N.nbits()-rlen))
	r = ZZ.random_element(0,2^rlen)
	m = a+r
	c = lift(mod(m,N)^d)

	x = ZZ['x'].0
	f = (x+a)^d-c
	X = 2^rlen
	return (f,N,X),r

def test_coppersmith():
	(f,N,X),r = gen_random_coppersmith()
	print(f)
	print(N)
	print(X)
	u = univariate_coppersmith(f,N,X)
	print(u.solve())
	if r in u.solve():
		print "Success!"
	else:
		print "Failure. :("

def solve(f, N, X):
	u = univariate_coppersmith(f,N,X)

	return u.solve()[0]

N = 799435724361941209634642555902315435908058123605331438387001798549338453520550411955040034588382681734261551948934231708112188214329385775197475015900886462678223823221663504870303417810891914590183627695363822581523705641504085155996223051520822630001053204808158568793360428631925512479398108990194783353106281215727815924117572620057685972399090366983671158515878975809439859039986317907669857201927700624787846399742932381426050450874840002845772010595287785787014208146359876931886263687047818683794261329936228163632966638728420728815223888138456007423954834668594012507643531951685321953112783259102186136667

e = 3

c = 0x1396c4db226f20a9076f0197826de0220f57cc4359107111b9eebf5e56b52e43e70aa2371b4db64260f0bbad80db0c7f8a121997bb02667a3d2d40d0e086209cd6e18568e251331a536d35257ae57bb7824e8dfbc6d1d1b421eab40ddfef686d8882806e44c353cc9efc2576c76ab856c7c2dbf27e43e2cc61da3f0aee94ed426f3b646981f60a965c9abe80bb09ea5def3db33929b1696d36f773c09989e511d7e16c99ddbe104331cd25e585483469ffeed7dbea1f2c829ed02eb98d6f4cb63ba67bc2aab0ddb44ef218141acd4a6ae14efa3dbf7d2834a6a40d054f1b0c49b757dabb75c5b91d6f415fe5c1e35d9f8a72200ac6a198279bde3e76eb5face

a = Integer(int('20'*97+'00'*31, 16))

x = ZZ['x'].0

f = (x+a)^e - c

X = 2^(31*8)

sol = solve(f, N, X)
print(sol)

print('FLAG =', long_to_bytes(sol))