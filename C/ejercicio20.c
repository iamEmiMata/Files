// Estructuras anidadas
#include <stdio.h>
#define length 2

// Agenda
struct agenda {
	char nombre[20], direccion[20], email[20], telf[12];
} contacto[length];


int main() {
	
//	introducimos los datos
	for(int datos = 0; datos < length; datos++){
		printf("Contacto #%i\n", datos+1);
		
		printf("Nombre : ");
		scanf("%s", &contacto[datos].nombre);
		
		printf("Direccion : ");
		scanf("%s", &contacto[datos].direccion);
		
		printf("Correo Electronico : ");
		scanf("%s", &contacto[datos].email);
		
		printf("Telefono : ");
		scanf("%s", &contacto[datos].telf);
		
		printf("\n\n");
	}
	
	
//	leemos los datos
	for(int datos = 0; datos < length; datos++){
		printf("\n\nContacto #%i", datos+1);
		
		printf("\nNombre : %s", contacto[datos].nombre);
		printf("\nDireccion : %s", contacto[datos].direccion);
		printf("\nCorreo : %s", contacto[datos].email);
		printf("\nTelefono : %s", contacto[datos].telf);
	}

	return 0;
}