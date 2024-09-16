#include "kakor.h"

long long cookies(int N, int A[]) {
    long long total = 0;
    for (int i = 0; i < N; i++) total += A[i];
    return total;
}
