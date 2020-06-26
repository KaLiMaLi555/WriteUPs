**itsy-bitsy**

The code takes two inputs `lower_bound=i>0` and `upper_bound=j>i>0`. Then takes a random number between 2\*\*i and 2\*\*j-1 computes xor with the flag bits.

```
def generate_random_bits(lower_bound, upper_bound, number_of_bits):
    bit_str = ''
    while len(bit_str) < number_of_bits:
        r = randint(lower_bound, upper_bound)
        bit_str += bin(r)[2:]
    return bit_str[:number_of_bits]

def bit_str_xor(bit_str_1, bit_str_2):
    xor_res = ''
    for i in range(len(bit_str_1)):
        bit_1 = bit_str_1[i]
        bit_2 = bit_str_2[i]
        xor_res += str(int(bit_1) ^ int(bit_2))
    return xor_res
```

So, I wrote a script that connects the server and sends `i=ind` and `j=ind+1` as where ind=range(0, len(flag_bits)). As the flag gets xored with binary of randint(2\*\*i, 2\*\*j-1), the leading bit of the number is always 1
```
Eg. i=5 and j=6
bin(randint(2**5, 2**6)) = 0b111010
bin(randint(2**5, 2**6)) = 0b111101
```

Using, the above property I created the script

```
from pwn import *

flag_bits = ''

for ind in range(1,300):
	p = remote('2020.redpwnc.tf', 31284)
	log.info('Connecting {0} times'.format(ind))
	data = p.recv().decode()
	# log.info(data + '1')
	p.sendline(str(ind))

	data = p.recv().decode()
	# log.info(data + '2')
	p.sendline(str(ind+1))

	data = p.recv().decode()
	# log.info(data)

	ct = data.strip().split(': ')[-1]

	if ind == 1:
		flag_bits += ct[:2]


	if ct[ind+1] == '0':
		flag_bits += '1'
	else:
		flag_bits += '0'


flag = ''

for i in range(0, len(flag_bits), 7):
	flag += chr(int(flag_bits[i:i+7], 2))

flag = 'f' + flag[1:-1] + '}'

print(flag)
```

FLAG: `flag{bits_leaking_out_down_the_water_spout}`