#include <conio.h>
#include <stdio.h>


int main() {
	int edad, limite = 18;
	printf(":: PARENTAL CONTROL ::");
	printf("Introduce tu edad > ");
	scanf("%d", &edad);
	
	if(edad >= limite) {
		printf("Disponible!");
	} else {
		printf("Lo siento, Este contenido es solo para mayores 18+");
	}
	
	return 0;
}