**bubbly**

The decompiled code for main shows that the code simply asks for a input(index < 8 for some array nums) and swaps the values at [index] and [index+1]

![alt text](https://github.com/KaLiMaLi555/WriteUPs/blob/master/redpwn2020/rev/bubbly/images/main.png)

Using gdb I get the initial value of nums
`$1 = {1, 10, 3, 2, 5, 9, 8, 7, 4, 6}`

So, I implemented a simple bubble sort in python
```
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
```
