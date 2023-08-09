#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 5000001;

string T, P;                       // T = text, P = pattern
typedef vector<int> vi;

// credits to CP4 repository
int b[MAX_N];                                    

void kmpPreprocess() {                           
    int i = 0, j = -1; b[0] = -1;                 
    while (i < P.length()) {                                
        while ((j >= 0) && (P[i] != P[j])) j = b[j]; 
        b[++i] = ++j; 
    }
}

vi kmpSearch() {
    vi occ;                            
    int i = 0, j = 0;                              
    while (i < T.length()) {                                
        while ((j >= 0) && (T[i] != P[j])) j = b[j]; 
        ++i; ++j;                                    
        if (j == P.length()) {                                
            occ.push_back(i - j);
            j = b[j];                                 
        }
    }
    return occ;
}

void printVector(vi& v) {
    for (int i = 0; i < v.size(); i++) {
        cout << v[i];
        if (i < v.size() - 1) cout << " ";
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (getline(cin, P)) {
        getline(cin, T);
        for (int i = 0; i < P.length(); i++) b[i] = 0;
        kmpPreprocess();
        vi occ = kmpSearch();
        printVector(occ);
    }
    return 0;
}