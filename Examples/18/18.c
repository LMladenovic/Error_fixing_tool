#include <stdlib.h>
#include <stdio.h>

int main( void ){
	int *t = calloc(sizeof(int), 2);
	
	printf("%d\n", t[3]);
	return 0;
}
