// Ciclo While
#include <stdio.h>

int main() {
	int i = 1;
	printf("Num 1 al 10 incremento  \n");
	while (i <= 10) {
		printf("%i \t", i);
		i++; // incremento
	}
	
	printf("\nNum 1 al 10 decremento  \n");
	int x = 10;
	while (x > 0) {
		printf("%i \t", x);
		x--; // decremento
	}
	
	printf("\nNum Pares 1 al 10  \n");
	int z = 2;
	while (z <= 10) {	
		printf("%i \t", z);
		z = z + 2; // incrementa de 2 en 2
	}
	
	printf("\nNum Inpares 1 al 10  \n");
	int j = 1;
	while (j <= 10) {	
		if(j % 2 != 0) {
			printf("%i \t", j);
		}
		j++;
	}
	
	return 0;            
}
                                   