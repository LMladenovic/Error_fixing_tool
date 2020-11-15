#include <stdio.h>
#include <stdlib.h>


int mod(int a){
	return a % 33;
}

void print_and_free(){
	float *t = malloc(sizeof(float));
	*t  = 0;
	
	printf("%f\n", *t);
	free(t);
}

void vector_addition(double *x1, double *x2){
	int i;
	printf("Addition of vectors [1,2,3,4,5] and [-5, -4, -3, -2, -1] is:\n [");
	for(i=0;i<=5;i++){
		printf("%lf ", x1[i]+x2[i]);
	}
	printf("]\n");
	free(x1);
	free(x2);
}

int main(){
	int x= 0;

	printf(" %d mod 33 is %d\n", x, mod(x));

	print_and_free();

	double *x1 = malloc( sizeof(double)*6 );
	int __index1__;
	for( __index1__ = 0; __index1__ < 6; __index1__ ++)
		x1[__index1__] = 0;
	double *x2 = malloc( sizeof(double)*6 );
	int __index__;
	for( __index__ = 0; __index__ < 6; __index__ ++)
		x2[__index__] = 0;

	int i;

	for (i=0; i<=4; i++){
		x1[i] = (i+1)*1.0;
		x2[i] = -(5- i) *1.0;
	}

	vector_addition(x1,x2);	



	return 0;
}
