int printf(char* a, ...);
int scanf(char* a, ...);

const int N = 1e5 + 10, M = 1e6 + 10;

void getNext(int n, char p[], int next[]){
    next[0] = 0;
    for(int j = 0, i = 1; i < n; i++){
        while(j && p[i] != p[j])    j = next[j - 1];
        if(p[i] == p[j])            j++;
        next[i] = j;
    }
}


int main(){
    int n, m, next[N];
    char p[N], s[M];

    // cin >> n >> p;
    // cin >> m >> s;

    // if (n > m) {
    //     cout << "n is larger than m" << endl;
    //     return -1;
    // }

    getNext(n, p, next);
    
    for(int i = 0, j = 0; i < m; i++){
        while(j && s[i] != p[j])    j = next[j - 1];
        if(s[i] == p[j])            j++;
        if(j == n){
            cout << i - n + 1 << ' ';
            j = next[j - 1];
        }
    }
    
    return 0;
}   