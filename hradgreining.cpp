#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 200010;

string T, P;                       // T = text, P = pattern

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
    P = "COV";
    cin >> T;
    kmpPreprocess();
    cout << ((kmpSearch() > 0) ? "Veikur!\n" : "Ekki veikur!\n");
    return 0;
}