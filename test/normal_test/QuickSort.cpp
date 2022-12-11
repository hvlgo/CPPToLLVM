int printf(char* a, ...);
int scanf(char* a, ...);

int N;

int q[100];

void quick_sort(int l,int r)
{
    int i = l - 1, j = r + 1;
    int x = q[(l+r)/2];
    if (l >= r) 
        return;
    while (i < j) {
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if(i < j) {
            int tmp = q[i];
            q[i] = q[j];
            q[j] = tmp;
        }
            
    }
    quick_sort(l, j);
    quick_sort(j + 1, r);
}
    
int main()
{   
    printf("enter N(<100):");
    scanf("%d", &N);
    // cin>>n;
    for (int i = 0; i < N; i++)
        // cin >> q[i];
        scanf("%d", &q[i]);
    quick_sort(0, N - 1);
    for (int i = 0; i < N; i++)
        printf("%d ", q[i]);
        // cout << q[i] << " ";
    return 0;
}
