from pwn import *

# flag_bits = '0100110110110011000011100111111101111000101101001111010011100111011111110110011001011100001110101111010011101110110011110111111101111111010111101001011111110010011011111110111110111010111111110100110100011001011011111111011111000011110100110010111100101011111111001111100001101111111010111101001111101'

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