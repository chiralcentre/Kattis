#include <bits/stdc++.h>

using namespace std;

unordered_map<string,string> ans = {{"Reykjavik", "Reykjavik"}, {"Kopavogur", "Reykjavik"}, {"Hafnarfjordur", "Reykjavik"},
{"Reykjanesbaer", "Reykjavik"},{"Akureyri", "Akureyri"},{"Gardabaer", "Reykjavik"},
{"Mosfellsbaer", "Reykjavik"},{"Arborg", "Reykjavik"}, {"Akranes", "Reykjavik"},
{"Fjardabyggd", "Akureyri"}, {"Mulathing", "Akureyri"}, {"Seltjarnarnes", "Reykjavik"}};

string s;

int main() {
    cin >> s;
    cout << ans[s] << "\n";
    return 0;
}