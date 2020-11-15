#include <stdlib.h>
#include <unistd.h>

int main( void ){
  char* arr  = calloc( sizeof(char), 10);
  int*  arr2 = malloc(sizeof(int));
  write( 1 /* stdout */, arr, 10 );
  exit(0);
}
