#include <stdlib.h>
#include <stdio.h>

int main( void ){
	int *t = malloc(sizeof(int));
	t = realloc(t, 2*sizeof(int) +  4*sizeof(int));
	int __index__;
	for( __index__ = 0; __index__ < 6; __index__ ++)
		t[__index__] = 0;


	printf("%d\n", t[5]);
	return 0;
}
