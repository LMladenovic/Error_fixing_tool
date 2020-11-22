#include <stdlib.h>
#include <stdio.h>

int main( void ){
	int *t = malloc(sizeof(int));
	t = realloc( t, -2*sizeof(int));
	printf("%d\n", t[3]);
	return 0;
}
