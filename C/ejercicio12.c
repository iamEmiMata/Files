#include <stdio.h>

int main(){
	
	int num = 0;
	while (num <= 7) {
		
		if(num == 2){
			continue;
		}
		printf("%i\n", num);
		num++;
	}
	
	return 0;
}