#include <stdio.h>
#include <stdlib.h>

int main(int argv, char** argc){
	char *r = malloc(abs(-15));
	int *t = malloc(3);
	t = (int *)realloc(t,abs( -3*sizeof(int))); 
	free(r);
	free(t);
	return 0;

}
