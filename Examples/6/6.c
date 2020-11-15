#include <stdio.h>
#include <stdlib.h>


int mod(int a){
	return a % 33;
}

void print_and_free(){
	float *t = malloc(sizeof(float));
	
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
	int x;

	printf(" %d mod 33 is %d\n", x, mod(x));

	print_and_free();

	double *x1 = malloc( sizeof(double)*4);
	double *x2 = malloc( sizeof(double)*4);

	int i;

	for (i=0; i<=4; i++){
		x1[i] = (i+1)*1.0;
		x2[i] = -(5- i) *1.0;
	}

	vector_addition(x1,x2);	
	free(x1);
	free(x2);

	return 0;
}
