from pwn import *
from z3 import *
from hashlib import *

def matmul(A, B):

	result = [[0]*len(A[0])]*len(A)

		# iterating by row of A 
	for i in range(len(A)): 
	  
		# iterating by coloum by B  
		for j in range(len(B[0])): 
	  
			# iterating by rows of B 
			for k in range(len(B)): 
				result[i][j] += A[i][k] * B[k][j] 

	return result


def transpose(A): 
	B = A[:][:]

	for i in range(len(A)): 
		for j in range(len(A[0])): 
			B[i][j] = A[j][i]

	return B


p = remote('76.74.178.201', 8001)

log.info(p.recv().decode())
log.info(p.recvuntil('------------------------------------------------------------------------\n').decode())

while True:
	log.info(p.recvline().decode())
	
	data = p.recvuntil('|').decode().strip()[:-1].strip()

	log.info(p.recv())

	log.info(data)
	mat = data.split('\n')

	A = []
	i = 0
	j = 0

	s = Solver()

	for row in mat:
		d = row.replace('[', '').replace(']', '')
		d = d.split(',')
		A.append([])

		j = 0
		for num in d:
			if '?' in num:
				A[i].append(Int(f'M_{i}_{j}'))
				s.add(Or(A[i][j] == 1, A[i][j] == -1))
			else:
				A[i].append(int(num))
			j += 1
		i += 1

	
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

		for i in range(len(A)):
			for j in range(len(A[0])):
				if not isinstance(A[i][j], int):
					A[i][j] = m[A[i][j]]

		print(A)

		p.sendline(md5(str(A).encode()).hexdigest())

		log.info(p.recvline())

	else:
		print('Nothing Here')

	# break

