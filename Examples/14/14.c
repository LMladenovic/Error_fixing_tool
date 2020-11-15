#include <stdio.h>
#include <stdlib.h>

int main(){

	int *t = malloc(4*sizeof(int));

	printf("Right side overdraft: %d\n", t[4]);
	printf("Left side overdraft: %d\n", t[4-5]);
	free(t); 
	return 0;
}
