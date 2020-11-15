#include <stdio.h>
#include <stdlib.h>


int sum(int a, int b){
	return a + b;
}

void print_and_free(int *t){
	int i;
	for (i =0;i<7; i++)
		printf("%d  ", t[i]);
	printf("\n");
	free(t);
	
}

int main(int argc, char **argv){

	int i;

	printf("Command line arguments: \n");
	for (i=0;i<argc;i++)
		printf("%s ", argv[i]);
	printf("\n");

	int x;

	printf("Sum of numbers %d and %d is %d\n", x, 5, sum(x, 5));

	x = 5;
	int *t = malloc(sizeof(int)*x);

	for (i =0;i<6; i++){
		if ((i+1)%2 ==0)
			t[i] = (i+1)*(i+1);
		else
			t[i] = (i+1)*(i+1)*(i+1);
	}

	print_and_free(t);
	free(t);



	return 0;
}
