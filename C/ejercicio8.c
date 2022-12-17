// Switch
#include <stdio.h>

int main() {
	int opcion;
	printf(":: COLORES EN INGLES :: \
	\nElige un color de la lista\
	\n 1. blanco \t 2. Negro \t 3. Rojo \t 4. Amarillo \t 5. Azul\n\n> ");
	scanf("%i", &opcion);
	
	switch(opcion){
		case 1:
		printf("Blanco en ingles es White");
		break;
		
		case 2:
		printf("Negro en ingles es Black");
		break;
		
		case 3:
		printf("Rojo en ingles es Red");
		break;
		
		case 4:
		printf("Amarillo en ingles es Yellow");
		break;
		
		case 5:
		printf("Azul en ingles es Blue");
		break;
		
		default:
		printf("La opcion que elegiste no se encuentra en la lista");
		break;
	}
	
	return 0;
}