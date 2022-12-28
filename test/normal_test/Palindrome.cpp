int printf(char* a, ...);
int scanf(char* a, ...);



char str[100];
int N;

void check()
{
	printf("please enter your string length:\n");
	scanf("%d", &N);
	printf("please enter your string:\n");
	scanf("%s", str);

	int flag = 1;
	int front = 0;
	while(front < N)
	{
		if(str[front] != str[N-1])
			flag = 0;
		front = front + 1;
		N = N - 1;
	}
	if(flag)
		printf("true\n");
	else
		printf("false\n");

}

int main(){
	check();
	return 0;
}