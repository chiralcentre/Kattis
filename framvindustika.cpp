#include <bits/stdc++.h>

using namespace std;

int main() {
    int p,w; scanf("%d %d",&p,&w);
    int f = w * p / 100, L = to_string(p).length();
    string s = "[";
    for (int i = 0; i < f; i++) s.push_back('#');
    for (int i = 0; i < w - f; i++) s.push_back('-');
    s.append("] |");
    for (int i = 0; i < 4 - L; i++) s.push_back(' ');
    s.append(to_string(p));
    s.push_back('%');
    printf("%s\n",s.c_str());
    return 0;
}