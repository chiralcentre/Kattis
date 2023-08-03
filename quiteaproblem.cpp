#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 200010;

string T, P;                       // T = text, P = pattern

// Knuth-Morris-Pratt's algorithm specific code
int b[MAX_N];                                    // b = back table

void kmpPreprocess() {                           // call this first
  int i = 0, j = -1; b[0] = -1;                  // starting values
  while (i < P.length()) {                                // pre-process P
    while ((j >= 0) && (P[i] != P[j])) j = b[j]; // different, reset j
    b[++i] = ++j; //advance both i and j
  }
}

int kmpSearch() {                               // similar as above
  int freq = 0, i = 0, j = 0;                              // starting values
  while (i < T.length()) {                                // search through T
    while ((j >= 0) && (T[i] != P[j])) j = b[j]; // if different, reset j
    ++i; ++j;                                    // if same, advance both
    if (j == P.length()) {                                // a match is found
      ++freq;
      j = b[j];                                  // prepare j for the next
    }
  }
  return freq;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    P = "problem";
    kmpPreprocess();
    while (getline(cin, T)) {
        transform(T.begin(), T.end(), T.begin(), ::tolower); // transform string to lower case
        int res = kmpSearch();
        cout << ((res > 0) ? "yes\n" : "no\n");
    }
    return 0;
}