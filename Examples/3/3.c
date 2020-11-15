#include<stdio.h>
#include <stdlib.h>


int  main (){
	int x = 3;
	int *t = malloc ( sizeof( int )*4) ;
	int  y = x + t[5] ;
	printf("%d\n", y);

	free(t);
	return  0;
}
