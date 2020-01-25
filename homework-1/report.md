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
### Solution
### Code
### Help Received
