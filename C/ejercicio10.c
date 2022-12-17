// Arreglos
#include <stdio.h>

int main() {
	
	int size; 
	printf("Arreglo N : \n>	");
	scanf("%i", &size);
	int v[size];
	for(int x = 0; x < size; x++){
		printf("posicion v[%x]\n", x+1);
		scanf("%i", &v[x]);
	}
	printf("Array\n");
	for (int x = 0; x < size; x++){
		printf("v['%i']\t", v[x]);
	}
	return 0;
}