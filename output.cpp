int printf(char* a, ...);
int scanf(char* a, ...);


int main(){
	int a = 1;
	do {
		printf("%d ", a);
		a = a + 1;
	} while (a != 5);

	int b = 1;
	do {
		printf("%d ", b);
		b = b + 2;
	} while (b < 23);
	return 0;
}