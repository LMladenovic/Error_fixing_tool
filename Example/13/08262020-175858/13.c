#include <stdio.h>
#include <stdlib.h>

typedef struct _point{
int x;
int y;
int consts[3];
}Point;

int main(){
	int *t= NULL;
	Point *A= NULL;
	int x[3];
	int __index__;
	for( __index__ = 0; __index__ < 3; __index__ ++)
		x[__index__] = 0;
	float rN= 0;

//	printf("Point A(%d,%d)\n", A->x, A->y);
	printf("%d\n", t);

	int i;
	for (i=0;i<3;i++)
		printf("x[%d] = %d\n", i+1, x[i]);

	printf("%f\n", rN);
	return 0;
}
