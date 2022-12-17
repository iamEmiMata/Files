// arreglo multidimensional
#include <stdio.h>

int main() {
	int array[2][3] = {{1,2,3},{8,7,6}};
	printf("Array 2x3 : \narray[0][1] : %i", array[0][1]); // accedemos al num 2
	printf("\narray[1][2] : %i", array[1][2]); // accedemos al num 6
	return 0;
}