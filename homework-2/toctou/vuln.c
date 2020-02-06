#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUFSIZE 128
#define FLAGSIZE 128

void win(char *filename) {
  char buf[FLAGSIZE];
  FILE *f = fopen(filename,"r");
  fgets(buf,FLAGSIZE,f);
  puts(buf);
  fflush(stdout);
}

void vuln() {
  char filename[BUFSIZE];
  struct stat sb;
  int len;
  printf("Please enter a filename\n");
  fgets(filename,BUFSIZE,stdin);

  len=strlen(filename);
  if(filename[len-1]=='\n') filename[len-1]='\0';

  if (strstr(filename,"flag")!=NULL) {
     printf("No, you can't have that one!\n");
     return;
  }
  if (lstat(filename,&sb)!=0) {
     printf("Bad file!\n");
     return;
  }
  if (S_ISLNK(sb.st_mode)) {
     printf("Nice try linking to the flag!\n");
     return;
  }
  printf("I guess I'll let you have that one, but you'll have to wait for it\n");
  fflush(stdout);
  sleep(1);
  win(filename);
  fprintf(stderr,"done!\n");
}

int main(int argc, char **argv){
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  int saved_flags;
  setresgid(gid, gid, gid);

  //setvbuf(stdin, NULL, _IONBF, 0);
  //saved_flags = fcntl(1, F_GETFL);

// Set the new flags with O_NONBLOCK masked out

  //fcntl(1, F_SETFL, saved_flags & ~O_NONBLOCK);
  vuln();
  return 0;
}
