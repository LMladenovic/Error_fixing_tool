#include <stdio.h>
#include <stdlib.h>

typedef struct _point{
int x;
int y;
int consts[3];
}Point;

int main(){

	Point A;

	Point B[5];

	printf("Point A(%d,%d)\n", A.x, A.y);
	
	int i;
	for (i=0;i<5;i++)
		printf("B[%d] = (%d, %d)\n", i+1, B[i].x, B[i].y);

	return 0;
}
