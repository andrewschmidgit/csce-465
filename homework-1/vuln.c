#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>
#include <time.h>

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
   // Only initialize the PRNG once
   // https://stackoverflow.com/questions/5574914/srandtimenull-doesnt-change-seed-value-quick-enough
   srand(time(NULL));
   unsigned int num;
   unsigned int inputnum, count=0;
   while (count<10) {
      num = random()%100;
      printf("What number am I thinking of?\n");
      scanf("%u",&inputnum);
      if (inputnum!=num) {
         printf("Nice try!\n");
         exit(0);
      }
      else {
         printf("You got lucky that time!\n");
	 count++;
      }
   }
   printf("Wow! You must be psychic! Ok, here's the flag\n");
   win();
}
