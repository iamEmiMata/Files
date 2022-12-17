#include <stdio.h>

int suma();
int main() {
	printf("\nSuma = %i", suma());
	return 0;
}

int suma() {
	int num1, num2, suma;
	printf("Numero 1 > ");
	scanf("%i", &num1);
	printf("Numero 2 > ");
	scanf("%i", &num2);
	
	suma = num1 + num2;
	return suma;
}