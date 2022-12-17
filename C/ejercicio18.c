// Arreglos

#include <stdio.h>

struct persona {
	char nombre[30], curso[30];
	int nota;
} person[3]; // Dimension fxc : 3x3

int main() {
	
//	Anhadimos los datos al array
	for (int array = 0; array < 3; array++){
		printf("\n\n%i Nombre : ", array+1);
		scanf("%s", &person[array].nombre);
		
		printf("%i Curso : ", array+1);
		scanf("%s", &person[array].curso);
		
		printf("%i Calificacion : ", array+1);
		scanf("%i", &person[array].nota);
	}
	
//	Muestra los datos dentro del array
	printf("\n\n::DATOS::");
	for (int array = 0; array < 3; array++) {
		printf("\nNombre : %s", person[array].nombre);
		printf("\tCurso : %s", person[array].curso);
		printf("\tCalificacion : %i", person[array].nota);
	}
	
	
	
	return 0;
}