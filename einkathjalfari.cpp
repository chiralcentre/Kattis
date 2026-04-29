#include <iostream>
#include <sstream>
#include <string>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

template <class T>
using ordered_set = tree<
    T,
    null_type,
    less<T>,
    rb_tree_tag,
    tree_order_statistics_node_update>;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    cin.ignore(); // consume leftover newline
    ordered_set<int> s;

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        stringstream ss(line);
        char type;
        ss >> type;
        int x,y;
        if (type == 'A') {
            ss >> x;
            s.insert(x);
        } else if (type == 'F') {
            ss >> x >> y;
            int b = s.order_of_key(y + 1) - s.order_of_key(x);
            cout <<  y - x + 1 - b << "\n";
        } else if (type == 'D') {
            ss >> x;
            s.erase(x);
        }
    }
    return 0;
}