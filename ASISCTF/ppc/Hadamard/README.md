# Hadamard

![alt text](https://github.com/KaLiMaLi555/WriteUPs/blob/master/ASISCTF/ppc/Hadamard/images/hadamard.png)

After connecting to the server, we see a message explaining the task
![alt text](https://github.com/KaLiMaLi555/WriteUPs/blob/master/ASISCTF/ppc/Hadamard/images/main.png)

From above, its clear that the server is asking us to fill the matrix and send in its md5 hash

It was a pretty straight forward challenge.
I thought of using z3-Solver for finding the missing matrix elements. The only missing thing here is what condition should I use. At first, I just used the conditions generated from `M * MT = nI`. I don't know why but that didn't work out every time. So, I read more about Hadamard Matrices on wikipedia and found this.

![alt text](https://github.com/KaLiMaLi555/WriteUPs/blob/master/ASISCTF/ppc/Hadamard/images/hadamard_wiki.png)

All rows of the matrix are supposed to be orthogonal, i.e, the dot product of each row must be **zero**.

So, I used this to generate new conditions. Below is the code snippet for the same.

```
## Additional condition that needs to be added is that 
## all elements of the array must be either 1 or -1

for i in range(0, len(A)-1):
	
	for k in range(i+1, len(A)):
		cond = None
		for j in range(len(A[0])):
			if cond == None:
				cond = A[i][j] * A[k][j]
			else:
				cond += A[i][j] * A[k][j]

		s.add(cond == 0)

print(s.check())
if s.check() == sat:
	m = s.model()
```

The actual can be found in the repo.


FLAG: `ASIS{iT5_7h3_ZO0_0F___Hadamard___M4Tr1c3S}`
