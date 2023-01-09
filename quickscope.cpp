#include <bits/stdc++.h>
#include <string>
#include <unordered_map>

using namespace std;

typedef vector<int> vi;
typedef unordered_map<string,string> ss;
typedef unordered_map<string,vi> svi;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    vector<ss> stack; svi types; ss curr;
    for (int i = 0; i < N; i++) {
        string a; cin >> a;
        if (a == "{") {
            stack.push_back(curr);
            curr = ss ();
        } else if (a == "}") {
            ss prev = curr;
            curr = stack.back(); stack.pop_back();
            for (auto &[key,value] : prev) {
                if (types[key].back() == stack.size() + 1) {
                    types[key].pop_back();
                }
            }
        } else if (a == "DECLARE") {
            string v,t; cin >> v >> t;
            if (curr.find(v) != curr.end()) {
                cout << "MULTIPLE DECLARATION\n";
                break;
            }
            curr[v] = t;
            if (types.find(v) != types.end()) {
                types[v].push_back((int) stack.size());
            } else {
                types[v] = vi {(int) stack.size()};
            }
        } else { //TYPEOF query
            string v; cin >> v;
            if (types.find(v) == types.end() || types[v].empty()) cout << "UNDECLARED\n";
            else {
                int lastIndex = types[v].back();
                cout << (lastIndex >= stack.size() ? curr[v] : stack[lastIndex][v])<< "\n";
            }
        }
    }
    return 0;
}