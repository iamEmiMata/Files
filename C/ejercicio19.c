// Estructuras anidadas

#include <stdio.h>
#define length 2

struct owner {
	char nombre[20];
	char direccion[30];
};

struct dog {
	char nombre[20];
	int edad;
	struct owner ownerDog;
} dogs[length];

int main() {
	
	for (int datos = 0; datos < length; ++datos){
		
		printf("\nNombre del perro : \n>	");
		scanf("%s", &dogs[datos].nombre);
		
		printf("\nEdad del perro: ");
		scanf("%i", &dogs[datos].edad);
		
		printf("\nNombre del duenho > ");
		scanf("%s", &dogs[datos].ownerDog.nombre);
		
		printf("\nDireccion > ");
		scanf("%s", &dogs[datos].ownerDog.direccion);
	}
	
	for (int datos = 0; datos < length; ++datos){
		printf("\nPedido: %s", pedido[datos].orden);
		printf("\tCliente: %s", pedido[datos].clientePedido.nombre);
		printf("\tDirrecion: %s", pedido[datos].clientePedido.direccion);
	}
	
	return 0;
}