int printf(char* a, ...);
int scanf(char* a, ...);

const int N=100000;

int q[N];

void quick_sort(int q[],int l,int r)
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
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}
    
int main()
{
    int n;
    scanf("%d", &n);
    // cin>>n;
    for (int i = 0; i < n; i++)
        // cin >> q[i];
        scanf("%d", &q[i]);
    quick_sort(q, 0, n - 1);
    for (int i = 0; i < n; i++)
        printf("%d ", q[i]);
        // cout << q[i] << " ";
    return 0;
}
