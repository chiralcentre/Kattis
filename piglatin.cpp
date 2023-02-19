#include <bits/stdc++.h>
#include <sstream>
#include <unordered_set>

using namespace std;

typedef vector<string> vs;

unordered_set<char> vowels({'a', 'e', 'i','o','u','y'});

int findIndexOfFirstVowel(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (vowels.find(s[i]) != vowels.end()) return i;
    }
    return -1;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string line;
    while (getline(cin, line)) {
        istringstream ss(line);
        vs words; string w;
        while (ss >> w) words.push_back(w);
        for (int i = 0; i < words.size(); i++) {
            string word = words[i];
            if (vowels.find(word[0]) == vowels.end()) { //begins with consonant
                int index = findIndexOfFirstVowel(word);
                cout << word.substr(index) << word.substr(0,index) << "ay";
            } else {
                cout << word << "yay";
            }
            if (i < words.size() - 1) cout << " ";
        }
        cout << "\n";
    }
    return 0;
}