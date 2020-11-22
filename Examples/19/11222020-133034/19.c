#include <stdlib.h>
#include <stdio.h>

int main( void ){
	int *t = malloc(sizeof(int));
	t = realloc( t, 2*sizeof(int) + abs( -2*sizeof(int)));
		int __index__;
	for( __index__ = 0; __index__ <  2*1 + abs( -2*1); __index__ ++)
		t[__index__] = 0;

	printf("%d\n", t[3]);
	return 0;
}
