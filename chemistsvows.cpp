#include <bits/stdc++.h>
#include <unordered_set>

using namespace std;

typedef unordered_set<string> us;

string s;

us elements({"h",  "he",
"li",  "be",                                          "b",  "c",  "n" ,  "o" ,  "f",  "ne",
"na",  "mg",                                          "al",  "si",  "p" ,  "s" ,  "cl",  "ar",
"k",  "ca",  "sc",  "ti",  "v",  "cr",  "mn",  "fe",  "co",  "ni",  "cu",  "zn",  "ga",  "ge",  "as",  "se",  "br",  "kr",
"rb",  "sr",  "y",  "zr",  "nb",  "mo",  "tc",  "ru",  "rh",  "pd",  "ag",  "cd",  "in",  "sn",  "sb",  "te",  "i",  "xe",
"cs",  "ba",  "hf",  "ta",  "w",  "re",  "os",  "ir",  "pt",  "au",  "hg",  "tl",  "pb",  "bi",  "po",  "at",  "rn",
"fr",  "ra",  "rf",  "db",  "sg",  "bh",  "hs",  "mt",  "ds",  "rg",  "cn",  "fl",  "lv",
"la",  "ce",  "pr",  "nd",  "pm",  "sm",  "eu",  "gd",  "tb",  "dy",  "ho",  "er",  "tm",  "yb",  "lu",
"ac",  "th",  "pa",  "u",  "np",  "pu",  "am",  "cm",  "bk",  "cf",  "es",  "fm",  "md",  "no",  "lr"}
);

string dp() {
    s = "*" + s; //pad string with one character at front
    vector<bool> possible(s.length(),false);
    possible[0] = true;
    for (int i = 1; i < s.length(); i++) {
        string base,intermediate; base += s[i];
        if (i >= 2) {
            intermediate += s[i - 1] + base;
            if (elements.find(intermediate) != elements.end() && possible[i - 2]) possible[i] = true;
        }
        if (elements.find(base) != elements.end() && possible[i - 1]) possible[i] = true;
    }
    return possible.back() ? "YES" : "NO";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T; cin >> T;
    while (T--) {
        cin >> s;
        cout << dp() << "\n";
    }
    return 0;
}