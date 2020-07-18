#include<stdio.h>
#include <stdlib.h>


int  main (){
	int  x;
	printf( "x = %d\n" , x) ;

	int *t = malloc ( sizeof( int )*4) ;
	float *u = malloc ( sizeof(float)*4) ;

	int  z = x + t[1] ;
	int y = z;

	printf("%d\n", y);
	
	printf( "t = %d %d %d \n" , t[1], t[2], *t) ;
	
	int i;

	for(i=0;i<4;i++)
		printf("u[%d] = %f\n", i, u[i]);
	
	free(t);
	free(u);
	return  0;
}
