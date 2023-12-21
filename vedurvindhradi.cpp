#include <bits/stdc++.h>

using namespace std;

int a,b;

int lower[13] = {0,3,16,34,55,80,108,139,172,208,245,285,327};
string cats[13] = {"Logn", "Andvari", "Kul", "Gola", "Stinningsgola",
                    "Kaldi", "Stinningskaldi", "Allhvass vindur", "Hvassvidri",
                    "Stormur", "Rok", "Ofsavedur", "Farvidri"};

int main() {
    scanf("%d.%d",&a,&b);
    a = a * 10 + b; 
    printf("%s\n", cats[upper_bound(lower, lower + 13, a) - lower - 1].c_str());
    return 0;
}