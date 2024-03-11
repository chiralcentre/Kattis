#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
//minimum number of adjacent swaps = number of inversions
//code runs in O(n log n) where n is number of elements
long mergeAndCountInv(int start, int mid, int end, vi &arr) {
    int size = end - start + 1;
    vi sortedArr(size,0);
    long invCount = 0;
    int leftIdx = start, rightIdx = mid + 1, idx = 0;
    //merge two sorted arrays into one sorted array
    while (leftIdx <= mid and rightIdx <= end) {
        if (arr[leftIdx] <= arr[rightIdx]) {
            sortedArr[idx++] = arr[leftIdx++];
            invCount += rightIdx - mid - 1;
        } else {
            sortedArr[idx++] = arr[rightIdx++];
        }
    }
    while (leftIdx <= mid) {
        sortedArr[idx++] = arr[leftIdx++];
        invCount += end - mid;
    }
    while (rightIdx <= end) sortedArr[idx++] = arr[rightIdx++];
    for (int i = start; i <= end; i++) arr[i] = sortedArr[i-start];
    return invCount;
}

long sortAndCountInv(int start,int end, vi &arr) {
    if (start == end) return 0;
    int mid = (end + start) / 2;
    return sortAndCountInv(start,mid,arr) + sortAndCountInv(mid + 1,end,arr) + mergeAndCountInv(start,mid,end,arr);
}

int main() {
    int N; scanf("%d",&N);
    vi arr(N,0);
    for (int i = 0; i < N; i++) scanf("%d", &arr[i]);
    printf("%ld\n",sortAndCountInv(0,N - 1,arr));
    return 0;
}