#include <stdio.h>
#include <stdlib.h>

int main(){

	int *t = malloc(4*sizeof(int) + 1*sizeof(int));
		int __index__;
	for( __index__ = 0; __index__ < 5; __index__ ++)
		t[__index__] = 0;


	printf("Right side overdraft: %d\n", t[4]);
	printf("Left side overdraft: %d\n", t[abs(4-5)]);
	free(t); 
	return 0;
}
