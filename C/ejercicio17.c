// Objecto = Struct

#include <stdio.h>

struct persona {
	char nombre[30], curso[30];
	float nota;
} p = {
	"Emilia",
	"Programacion",
	18.8	
};

int main() {
	
	printf("D A T O S \nNombre : %s \nCurso : %s \nNota : %f\n", p.nombre, p.curso, p.nota);
	return 0;
}