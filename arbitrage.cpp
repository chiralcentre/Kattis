#include <bits/stdc++.h>

using namespace std;

typedef tuple<int,int,double> iid;
typedef vector<iid> viid;
typedef unordered_map<string,int> msi;

const double INF = 1000000000;

double convert(string &s) {
    int i = s.find(':');
    int a = stoi(s.substr(0, i));
    int b = stoi(s.substr(i + 1));
    //take negation of natural logarithm of b/a
    return -log(double(b) / double(a));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    while (true) {
        int C; cin >> C;
        if (C == 0) break;
        msi mappings; 
        for (int i = 0; i < C; i++) {
            string s; cin >> s;
            mappings[s] = i;
        }
        int R; cin >> R;
        viid edgeList(R);
        for (int i = 0; i < R; i++) {
            string A,B,rate; cin >> A >> B >> rate;
            int u = mappings[A], v = mappings[B];
            double w = convert(rate);
            edgeList[i] = make_tuple(u,v,w);
        }
        //perform Bellman Ford in O(RC) time
        vector<double> D(C,INF); D[0] = 0;
        for (int i = 0; i < C - 1; i++) {
            for (iid edge: edgeList) {
                int u = get<0>(edge), v = get<1>(edge); double w = get<2>(edge);
                if (D[v] > D[u] + w) D[v] = D[u] + w;
            }
        }
        bool found = false;
        //relax all edges one more time to check for negative weight cycle
        for (iid edge: edgeList) {
            int u = get<0>(edge), v = get<1>(edge); double w = get<2>(edge);
            if (D[v] > D[u] + w) {
                found = true;
                break;
            }
        }
        cout << (found ? "Arbitrage\n" : "Ok\n");
    }
    return 0;
}