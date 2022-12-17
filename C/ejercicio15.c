#include <stdio.h>

void saludar(){
	int name[10];
	printf("Dime tu nombre : ");
	scanf("%s", &name);
	
	printf("\nHola %s - Saludos!", name);
	return;
}

int main() {
	
	saludar();
	return 0;
}