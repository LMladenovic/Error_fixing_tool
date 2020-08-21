#include <stdio.h>
#include <stdlib.h>

int main(){

	int b= 0;
	printf("Simple number: %d\n", b);

	int c[3];
	int __index__;
	for( __index__ = 0; __index__ < 3; __index__ ++)
			c[__index__] = 0;

	int k= 0;
	
	printf("Array:\n");
	for (k=0;k<3;k++)
		printf("%d ", c[k]);	

	int a[3][3];
	int __index2__;
	int __index3__;
	for( __index2__ = 0; __index2__ < 3; __index2__ ++)
		for( __index3__ = 0; __index3__ < 3; __index3__ ++)
				a[__index2__][__index3__] = 0;


	int i,j;
	
	printf("\nMatrix:\n");
	for (i=0;i<3;i++){
		for(j=0;j<3;j++)
			printf("%d ", a[i][j]);
		printf("\n");
	}

	return 0;
}
