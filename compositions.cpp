# include <bits/stdc++.h>

using namespace std;
typedef vector<int> vi;

int P,K,n,m,k;

int main() {
    scanf("%d",&P);
    for (int i = 0; i < P; i++) {
        scanf("%d %d %d %d",&K,&n,&m,&k);
        int total = (1 << (n - 1));
        if (m == 0) {
            if (n < k) printf("%d %d\n",K,total);
            else if (n == k) printf("%d %d\n",K,total - 1);
            else {
                vi compositions(n + 1, 0);
                compositions[0] = 1; compositions[1] = 1;
                for (int i = 2; i < k; i++) compositions[i] = (1 << (i - 1));
                compositions[k] = (1 << (k - 1)) - 1;
    			for (int i = k + 1; i <= n; i++) {
    				int cur_sum = 0;
    				for (int j = 1; j <= i; j++) {
    					if ((j % k) != 0) cur_sum += compositions[i-j];
    				}
    				compositions[i] = cur_sum;
    			}
    			printf("%d %d\n",K,compositions[n]);
            }
        } else {
            if (n < m) printf("%d %d\n",K,total);
            else if (n == m) printf("%d %d\n",K,total - 1);
            else {
                vi compositions(n + 1, 0);
                compositions[0] = 1; compositions[1] = 1;
                for (int i = 2; i < m; i++) compositions[i] = (1 << (i - 1));
                compositions[m] = (1 << (m - 1)) - 1;
    			for (int i = m + 1; i <= n; i++) {
    				int cur_sum = 0;
    				for (int j = 1; j <= i; j++) {
    					if ((j % k) != m) cur_sum += compositions[i-j];
    				}
    				compositions[i] = cur_sum;
    			}
    			printf("%d %d\n",K,compositions[n]);
            }
            
        }
        
    }
    return 0;
}