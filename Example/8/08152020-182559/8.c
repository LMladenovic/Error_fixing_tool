#include <stdio.h>
#include "8.h"


int main(){
	int a, b= 0;
	a = 5;
	int c= 0;
	printf("Sum called from .h file = %d \n", sum(a,b));
	printf("Sum counted directly = %d \n", a + c);
	return 0;

}
