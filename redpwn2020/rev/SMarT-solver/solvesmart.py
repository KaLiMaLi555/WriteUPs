from z3 import *
import re

FLAG_LEN = 73
flag = []

for i in range(FLAG_LEN):
	flag.append(BitVec('f_{0:02}'.format(i), 7))

file = open('assemblySmart.txt', 'r').read()

data = file.strip().split('\n')

data = [i.strip().split(' 	')[-1] for i in data]

conditions = []

conddict = {'jae': '<', 'jbe': '>'}

for i in range(0, len(data), 4):
	v1edx = re.findall("-(.*?)\(", data[i+0])[0]
	v2eax = re.findall("-(.*?)\(", data[i+1])[0]
	cond = data[i+3].split(' ')[0]


	indv1edx = FLAG_LEN - (int(v1edx, 16) - 0xd7)
	indv2eax = FLAG_LEN - (int(v2eax, 16) - 0xd7)

	try:
		if conddict[cond] == '<':
			conditions.append(flag[indv1edx] < flag[indv2eax])
		else:
			conditions.append(flag[indv1edx] > flag[indv2eax])
	except:
		print(v1edx, conddict[cond], v2eax)
		print(indv1edx, indv2eax)
		break

s = Solver()

for c in conditions:
	s.add(c)

for f in flag:
	s.add(f > 96)
	s.add(f < 126)

s.add(flag[0] == ord('f'))
s.add(flag[1] == ord('l'))
s.add(flag[2] == ord('a'))
s.add(flag[3] == ord('g'))
s.add(flag[4] == ord('{'))
s.add(flag[-1] == ord('}'))

if s.check() == sat:
	m = s.model()
	
	actual_flag = ''.join([chr((m[f].as_long())) for f in flag])
	print(actual_flag)
else:
	print('Nothing Here')