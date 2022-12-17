// Ciclo For
#include <stdio.h>

int main() {
	int i;
//	imprime los numeros del 1 al 10.
	printf("\nNumeros 1 al 10 Incremento\n");
	for (i = 1; i < 11; i++) {
		printf("%i \t", i);
	}
	
	printf("\n\nNumeros 1 al 10 Decremento\n");
	for (i = 10; i > 0; i--) {
		printf("%i \t", i);
	}
	
	printf("\n\nNumeros pares : 1 al 10 \n");
	for (i = 1; i < 11; i++){
		if(i % 2 == 0){
			printf("%i \t", i);
		}
	}
	
	printf("\n\nNumeros impares :  1 al 10 \n");
	for (i = 1; i < 11; i++){
		if(i % 2 != 0){
			printf("%i \t", i);
		}
	}
	
	return 0;
}
