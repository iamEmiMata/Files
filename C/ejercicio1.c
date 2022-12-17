#include <stdio.h>

int main() {
	char name[8];
	printf("Cual es tu nombre?\n>  ");
	scanf("%s", &name);
	printf("\nHola %s!", name);
	
	return 0;
}