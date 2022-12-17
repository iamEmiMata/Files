// Ciclo for con input
#include <stdio.h>

int main() {
	
	int i, edad;
	char nombre[10];
	for(i = 1; i < 3; i++) {
		printf("Nombre > ");
		scanf(" %s", &nombre);
		printf("Edad> ");
		scanf(" %d", &edad); // input
		
//		output
		printf("\nPersona #%i\nNombre y Edad \n", i);
		printf("%s de %i\n\n", nombre, edad);
	}
	
	return 0;
}