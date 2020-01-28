# Homework 1
> User: `vohtarak`
## PRNG
### Solution
Ran `exploit` in the background and `vuln` at the same time, wrote the seeded results to `numbers.txt`

### Code
```cpp
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <time.h>
#include <unistd.h>

#define FLAGSIZE 128


void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  fgets(buf,FLAGSIZE,f);
  puts(buf);
  fflush(stdout);
}

int main(int argc, char *argv[])
{
   srand(time(NULL));

   FILE *numbers = fopen("/home/vohtarak/homework-1/numbers.txt","w");
   for(int i = 0; i < 10; i++)
      fprintf(numbers, "%i: %li\n", i, random()%100);
   fclose(numbers);

   return 0;
}
```

### Help Received
- https://linux.die.net/man/3/fopen
- https://www.maketecheasier.com/run-bash-commands-background-linux/
- http://ctfweb.martincarlisle.com/problems

## Websniff
### Solution
1. Loaded the webpage
2. Opened Chrome Dev Tools to the `Network` tab
3. Reloaded to monitor network traffic
4. Looked at the main load request headers
![](packet-sniff.png)

### Help Received
- Chrome dev tools

## Brute Force Password
### Solution
run `john --wordlist=/usr/share/dict/words saltedpasswd.txt` and wait to output the password
### Help Received
https://www.openwall.com/john/doc/

## Known plaintext RSA
> unfinished
### Solution
I created a python script to loop through each of the encrypted messages, checking the message against the text (right padded with Ascii `0` character, then encrypted using the public key, then encoded in base64), however each time I ran `base64` the result would be different for the same string. Even `echo -ne "Hello World!" | openssl base64` would produce different results each time. 

But

### Code
```python
import os
import subprocess
from subprocess import PIPE
from itertools import islice

PRES_PUB_KEY = 'presidentpub.pem'
TRES_PUB_KEY = 'treasurypub.pem'

def getFilePath(filename):
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    return currentDirectory + '/' + filename

def openFile(filename, mode):
    return open(getFilePath(filename), mode)

def getEncrypted(text, pub_key):
    # Pad with null bytes
    text = text.ljust(214, chr(0))

    # use openssl rsautl
    rsa_result = subprocess.run(['openssl', 'rsautl', '-encrypt', '-pubin', '-inkey', pub_key], input=text.encode('utf-8'), stdout=PIPE).stdout

    # base64 encode
    encode_result = subprocess.run(['openssl', 'base64'], input=rsa_result, stdout=subprocess.PIPE).stdout

    return encode_result


banks = list(openFile("banks.txt", "r").readlines())
encryptedMessageLines = openFile("messages.txt", "r")

while True:
    message = ''.join(islice(encryptedMessageLines, 5))
    if not message:
        break
    crackedText = None
    for bank in banks:
        bank = bank.strip()
        clear = f'How much to {bank}?\n'
        encrypt = getEncrypted(clear, TRES_PUB_KEY).decode('utf-8')
        print(f'Bank: {bank}')
        print(f'clear: {clear}')
        print(f'encrypt: {encrypt}')
        print(f'message: {message}')
        
        if message == encrypt:
            crackedText = bank
            break
        exit()
    
    if crackedText is None:
        for i in range(1, 999):
            encrypt = getEncrypted('$' + str(i) + 'B\n', PRES_PUB_KEY)
            if message == encrypt:
                crackedText = bank
                break
    
    if crackedText is None:
        print('not today\n')
    else:
        print(crackedText)

encryptedMessageLines.close()
banks.close()
```
### Help Received
