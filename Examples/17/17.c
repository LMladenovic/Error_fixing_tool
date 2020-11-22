#include <stdlib.h>
#include <stdio.h>

int main( void ){
	int *t = malloc(sizeof(int));
	t = realloc(t, 4*sizeof(int));

	printf("%d\n", t[5]);
	return 0;
}
