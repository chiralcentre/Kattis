#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

const int MAX_N = 200010;

string T, P;                       // T = text, P = pattern
string pos[4] = {"A", "T", "G", "C"};

// credits to CP4 repository
int b[MAX_N];                                    

void kmpPreprocess() {                    
    int i = 0, j = -1; b[0] = -1;                 
    while (i < P.length()) {                                
        while ((j >= 0) && (P[i] != P[j])) j = b[j]; 
        b[++i] = ++j; 
    }
}

int kmpSearch() {                               
    int freq = 0, i = 0, j = 0;                              
    while (i < T.length()) {                                
        while ((j >= 0) && (T[i] != P[j])) j = b[j]; 
        ++i; ++j;                                    
        if (j == P.length()) {                                
        ++freq;
        j = b[j];                                 
        }
    }
    return freq;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (true) {
        cin >> P >> T; // string does not have spaces in it
        if (isdigit(P[0])) break;
        unordered_set<string> t2, t3;
        // generate all possibilities for type 2;
        for (int i = 0; i < P.length(); i++) t2.insert(P.substr(0,i) + P.substr(i + 1));
        // generate all possibilities for type 3;
        for (int i = 0; i <= P.length(); i++) {
            for (string p: pos) t3.insert(P.substr(0,i) + p + P.substr(i));
        }
        // get answers
        kmpPreprocess();
        int a1 = kmpSearch(), a2 = 0, a3 = 0;
        for (string s: t2) {
            P = s;
            for (int i = 0; i < P.length(); i++) b[i] = 0;
            kmpPreprocess();
            a2 += kmpSearch();
        }
        for (string s: t3) {
            P = s;
            for (int i = 0; i < P.length(); i++) b[i] = 0;
            kmpPreprocess();
            a3 += kmpSearch();
        }
        cout << a1 << " " << a2 << " " << a3 << "\n";
    }
    return 0;
}