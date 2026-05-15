#include <iostream>
#include <sstream>
#include <string>
#include <set>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string line;
    getline(cin, line);
    stringstream first(line);
    int n,k;
    first >> n >> k;
    set<pair<int,int>> s;
    getline(cin, line);
    stringstream ss(line);
    for (int i = 0; i < k; i++) {
        int c; 
        ss >> c;
        s.insert({c, i});
    }
    for (int i = 0; i < n; i++) {
        getline(cin, line);
        stringstream ss(line);
        char type;
        ss >> type;
        if (type == 'P') {
            pair<int,int> smallest = *s.begin();
            cout << smallest.first << "\n";
            s.erase(s.begin());
        } else if (type == 'S') {
            pair<int,int> largest = *s.rbegin();
            cout << largest.first << "\n";
            s.erase(prev(s.end()));
        } else if (type == 'C') {
            int c;
            ss >> c;
            s.insert({c, i + k});
        }
    }
    return 0;
}