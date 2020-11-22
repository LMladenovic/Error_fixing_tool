#include <stdio.h>
#include <stdlib.h>

typedef struct _point{
int x;
int y;
int consts[3];
}Point;

int main(){

	Point A;
	A.x=0;
	A.y=0;
	int __index__;
	for( __index__ = 0; __index__ < 3; __index__ ++)
		A.consts[__index__] = 0;

	Point B[5];
	int __index2__;
	for( __index2__ = 0; __index2__ < 5; __index2__ ++){
		B[__index2__].x=0;
		B[__index2__].y=0;
		int __index3__;
		for( __index3__ = 0; __index3__ < 3; __index3__ ++)
			B[__index2__].consts[__index3__] = 0;
		
	}

	printf("Point A(%d,%d)\n", A.x, A.y);
	
	int i;
	for (i=0;i<5;i++)
		printf("B[%d] = (%d, %d)\n", i+1, B[i].x, B[i].y);

	return 0;
}
