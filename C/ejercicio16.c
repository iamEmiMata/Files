#include <stdio.h>

// Apuntadores : Son variables cuyos valores son direcciones de memoria.

int main() {
	int a = 6;
	int *apuntador = &a;
	
	printf("%i\n", *apuntador);
	return 0;
}