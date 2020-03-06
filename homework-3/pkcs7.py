from pwn import *

context.log_level = 'error'

def xor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
def replace_str_index(text, index=0, replacement=''):
	return '%s%s%s'%(text[:index],replacement,text[index+1:])

desired = [
	'{"username": "gu',
	'est", "is_admin"',
	': "true", "expir',
	'es": "2021-01-01',
	'"}' + '\x0e'*14
]

iv = 'This is an IV456'

blocks = [
	iv,
	'a'*16,
	'a'*16,
	'a'*16,
	'a'*16,
	'a'*16,
]
for n in range(len(blocks)-2,-1,-1):
	for i in range(16):
		print 'Guessing ' , str(15-i), "th byte"
		for j in range(0,256):
			blocks[n] = replace_str_index(blocks[n], 15-i, chr(j))

			ciphertext = (blocks[n] + blocks[n+1]).encode('hex')

			while True:
				try:
					sleep(0.01)
					r = remote('ctfshell.martincarlisle.com', 47070)

					r.recvuntil('What is your cookie?\n')
					r.sendline(ciphertext)
					response = r.recv()
					r.close()
					break
				except:
					sleep(1)
					continue
			if response.find('invalid padding') == -1:
				for k in range(i+1):
					if i == 15:
						break
					new_val = chr(ord(blocks[n][15-k]) ^ (i+1) ^ (i+2))
					blocks[n] = replace_str_index(blocks[n], 15-k, new_val)
				print 'ciphertext:', ciphertext
				break

	blocks[n] = xor(blocks[n], '\x10'*16)
	blocks[n] = xor(blocks[n], desired[n])

print 'answer:', "".join(blocks).encode('hex')

