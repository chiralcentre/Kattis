#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<ll> vll;

ll arr[1000000], output[1000000],C[32768];

//perform counting sort for every block of 15 bits
void countingSort(int N, int k, int block) {
    for (int i = 0; i < k + 1; i++) C[i] = 0;
    int rightShift = block * 15;
    for (int i = 0; i < N; i++) C[(arr[i] >> rightShift) & k]++;
    //perform prefixSum computation
    for (int i = 1; i <= k; i++) C[i] += C[i - 1];
    //build sorted output
    for (int i = N - 1; i >= 0; i--) {
        output[C[(arr[i] >> rightShift) & k] - 1] = arr[i];
        C[(arr[i] >> rightShift) & k]--;
    }
    //copy sorted output over to arr
    for (int i = 0; i < N; i++) arr[i] = output[i];
}

//given integers fit within 30 bit range
//run 2 iterations of radix sort with 15 bits
void radixSort(int N) {
    for (int i = 0; i < 2; i++) countingSort(N,0b111111111111111,i);
}

int main() {
    int TC; scanf("%d",&TC);
    while (TC--) {
        int N; scanf("%d",&N);
        ll A,B,C; scanf("%lld %lld %lld",&A,&B,&C);
        ll X,Y; scanf("%lld %lld",&X,&Y);
        arr[0] = A;
        for (int i = 1; i < N; i++) arr[i] = (A + arr[i - 1] * B) % C;
        radixSort(N);
        ll V = 0;
        for (int i = 0; i < N; i++) V = (V * X + arr[i]) % Y;
        printf("%lld\n",V);
    }
    return 0;
}