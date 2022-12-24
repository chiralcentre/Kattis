#include <bits/stdc++.h>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

struct Cat {
    string name;
    int arrival, priority;

    Cat() {

    }

    Cat(string name, int arrival, int priority) {
        this->name = name;
        this->arrival = arrival;
        this->priority = priority;
    }
};

struct cmpCat {
    bool operator() (const Cat& a, const Cat& b) const {
        if (a.priority != b.priority) {
            return a.priority < b.priority;
        }
        return a.arrival > b.arrival;
    } 
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N; cin >> N;
    set<Cat,cmpCat> ts;
    unordered_map<string,Cat> hm;
    for (int i = 0; i < N; i++) {
        int q; cin >> q;
        if (q == 0) {
            string catName; int infectionLevel;
            cin >> catName >> infectionLevel;
            Cat c(catName,i,infectionLevel);
            hm[catName] = c;
            ts.insert(c);
        } else if (q == 1) {
            string catName; int u;
            cin >> catName >> u;
            Cat pc = hm[catName]; ts.erase(pc);
            Cat nc(catName,pc.arrival,pc.priority + u);
            ts.insert(nc); hm[catName] = nc;
        } else if (q == 2) {
            string catName; cin >> catName;
            ts.erase(hm[catName]);
        } else {
            if (ts.empty()) cout << "The clinic is empty";
            else {
                auto rit = *ts.rbegin();
                cout << rit.name;
            }
            cout << "\n";
        }
    }
    return 0;
}