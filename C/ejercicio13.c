#include <stdio.h>

long Factorial(long numero);
int main() {
	int numero;
	printf("Ingresa un numero\n>	");
	scanf("%i", &numero);
	
	for(int counter = 0; counter <= numero; counter++){
		printf("%d \t", Factorial(counter));
	}
	return 0;
}

long Factorial(long numero) {
	if(numero <= 1) {
		return 1;
	} else {
		return(numero * Factorial(numero-1));
	}
}