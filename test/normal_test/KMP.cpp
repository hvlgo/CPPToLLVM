int printf(char* a, ...);
int scanf(char* a, ...);

char p[100], s[100];
int next[100];

void getNext(int n){
    next[0] = 0;
    for(int j = 0, i = 1; i < n; i++){
        while(j && p[i] != p[j])    j = next[j - 1];
        if(p[i] == p[j])            j++;
        next[i] = j;
    }
}


int main(){
    int n, m;


    scanf("%d %d", &n, &p);
    scanf("%d %d", &m, &s);
    
    getNext(n);
    
    for(int i = 0, j = 0; i < m; i++){
        while(j && s[i] != p[j])    j = next[j - 1];
        if(s[i] == p[j])            j++;
        if(j == n){
            printf("%d ", i-n+1);
            j = next[j - 1];
        }
    }
    
    return 0;
}   