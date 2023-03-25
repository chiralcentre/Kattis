#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

void printLine(vii &list) {
    for (int i = 0; i < list.size(); i++) {
        ii p = list[i];
        int s = p.first, e = p.second;
        if (s == e) printf("%d",s);
        else printf("%d-%d",s,e);
        if (i == list.size() - 2) printf(" and ");
        else if (i < list.size() - 1) printf(", ");
    }
    printf("\n");
}

int main() {
    int C,N; scanf("%d %d",&C,&N);
    vi e(N,0);
    for (int i = 0; i < N; i++) scanf("%d",&e[i]);
    vii errors, correct;
    int start = e[0], prev = e[0]; ii pair(prev,prev);
    if (e[0] > 1) correct.push_back(make_pair(1,e[0] - 1));
    for (int i = 1; i < N; i++) {
        if (e[i] != prev + 1) {
            errors.push_back(pair);
            correct.push_back(make_pair(prev + 1, e[i] - 1));
            start = e[i];
            pair = make_pair(e[i],e[i]);
        } else pair = make_pair(start,e[i]);
        prev = e[i];
    }
    errors.push_back(pair);
    if (e.back() < C) correct.push_back(make_pair(e.back() + 1, C));
    printf("Errors: ");
    printLine(errors);
    printf("Correct: ");
    printLine(correct);
    return 0;
}