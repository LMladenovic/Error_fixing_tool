#include <stdio.h>
#include <stdlib.h>

int main(){

	int b;
	printf("Simple number: %d\n", b);

	int c[3];
	int k;
	
	printf("Array:\n");
	for (k=0;k<3;k++)
		printf("%d ", c[k]);	

	int a[3][3];

	int i,j;
	
	printf("\nMatrix:\n");
	for (i=0;i<3;i++){
		for(j=0;j<3;j++)
			printf("%d ", a[i][j]);
		printf("\n");
	}

	return 0;
}
