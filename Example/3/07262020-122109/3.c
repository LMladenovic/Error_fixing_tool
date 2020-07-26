#include<stdio.h>
#include <stdlib.h>


int  main (){
	int x = 3;
	int *t = malloc ( sizeof(int)*6 );
	int __index__;
	for( __index__ = 0; __index__ < 6; __index__  ++)
		t[__index__] = 0;
	int  y = x + t[5] ;
	printf("%d\n", y);

	free(t);
	return  0;
}
