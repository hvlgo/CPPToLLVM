#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

bool isPalindrome(string a) {
    string b = a;
	reverse(b.begin(), b.end());
	if (a == b) 
        return true;
	else 
        return false;
}

int main() {
	string a;
	cin >> a;
	cout << isPalindrome(a);
	return 0;
}
