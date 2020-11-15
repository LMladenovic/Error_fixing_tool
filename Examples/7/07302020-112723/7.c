#include<stdio.h>
#include <stdlib.h>


int  main (){
	int  x= 0;
	printf( "x = %d\n" , x) ;

	int t[4];
	int __index__;
	for( __index__ = 0; __index__ < 4; __index__ ++)
		t[__index__] = 0;

	float *u = malloc ( sizeof(float)*4) ;
	int __index1__;
	for( __index1__ = 0; __index1__ < 4; __index1__ ++)
		u[__index1__] = 0;


	int  z = x + t[1] ;
	int y = z;

	printf("%d\n", y);
	
	printf( "%d %d \n" , t[1], t[2]) ;
	
	int i;

	for(i=0;i<4;i++)
		printf("u[%d] = %f\n", i, u[i]);
	

	free(u);
	return  0;
}
