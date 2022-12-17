#include <conio.h>
#include <stdio.h>

int main() {
	int num1, num2, suma, resta, mult, div, resto;
	printf(":: OPERACIONES ARITMETICAS ::\n");
	
	printf("Numero 1 : ");
	scanf("%d", &num1);
	printf("Numero 2 : ");
	scanf("%d", &num2);
	
	suma = num1 + num2;
	resta = num1 - num2;
	mult = num1 * num2;
	div = num1 / num2;
	resto = num1 % num2;
	
	printf("Suma : %d\nResta : %d\nMultiplicacion: %d\nDivision: %d\nResto : %d\n",
	suma, resta, mult, div, resto);
	
	return 0;
}
