#include<stdio.h>
#include <stdlib.h>


int  main (){
	int x = 3;
	int *t = malloc ( sizeof( int )*4) ;
	t[5] = 15;
	printf("x = %d, t = %d\n",x, t[5]);

	free(t);
	return  0;
}
