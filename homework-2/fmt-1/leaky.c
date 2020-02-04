#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>


char buf[80];

int main (int argc, char **argv)
{

  unsigned int filler0 = 0x71751157;
  unsigned int key = ???;
  unsigned int filler1 = 0x71175015;
  unsigned int filler2 = 0x70075110;

  unsigned int red = read(STDIN_FILENO,buf,80);
  buf[red] = '\x00';
  printf(buf);
}
