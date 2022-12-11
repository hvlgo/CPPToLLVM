int printf(char* a, ...);
int scanf(char* a, ...);

char a[100];

void isPalindrome() {
    int flag = 1;
	int front = 0;
	int back = 0;
	while(a[back] != '\0')
		back = back + 1;
	back = back - 1;
	while(front < back)
	{
		if(a[front] != a[back])
			flag = 0;
		front = front + 1;
		back = back - 1;
	}
	if (flag) 
		printf("true\n");
        // return true;
	else 
		printf("false\n");
        // return false;
}

int main() {
	scanf("%s", a);
	// cin >> a;
	isPalindrome();
	// cout << isPalindrome(a);
	return 0;
}
