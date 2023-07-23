#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
#include <string>
#include <queue>

using namespace std;

typedef pair<int,double> id;
typedef pair<double,int> di;
typedef pair<double,double> dd;
typedef vector<double> vd;
typedef vector<di> vdi;
typedef vector<id> vid;
typedef vector<vid> vvid;
typedef vector<dd> vdd;
typedef unordered_map<string,int> msi;

const double INF = 1000000000;

double greatCircleDistance(double a, double b, double x, double y) {
    return 6381 * acos(cos(a) * cos(b) * cos(x - y) + sin(a) * sin(b));
}

double radians(double degrees) {
    return degrees * (M_PI / 180);
}

double modifiedDjikstra(vvid &adjList, int N, int s, int e) {
    vd D(N,INF); D[s] = 0;
    priority_queue<di,vdi,greater<di>> pq;
    pq.emplace(0,s);
    while (!pq.empty()) {
        auto [d,u] = pq.top(); pq.pop();
        if (u == e) return d;
        if (d == D[u]) {
            for (auto &[v,w]: adjList[u]) {
                if (D[v] > D[u] + w) {
                    D[v] = D[u] + w;
                    pq.emplace(D[v],v);
                }
            }
        }
    }
    return - 1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.precision(15);
    int N,M; cin >> N >> M;
    string S,T; cin >> S >> T;
    msi mappings; vdd coordinates(N); vvid adjList(N, vid {});
    for (int i = 0; i < N; i++) {
        string s; double la,lo; cin >> s >> la >> lo;
        coordinates[i] = make_pair(la,lo);
        mappings[s] = i;
    }
    for (int i = 0; i < M; i++) {
        string c,d; cin >> c >> d;
        int u = mappings[c], v = mappings[d];
        auto &[a,x] = coordinates[u]; auto &[b,y] = coordinates[v];
        double w = greatCircleDistance(radians(a),radians(b),radians(x),radians(y)) + 100;
        adjList[u].push_back(make_pair(v,w));
        adjList[v].push_back(make_pair(u,w));
    }
    cout << modifiedDjikstra(adjList,N,mappings[S],mappings[T]) << fixed << "\n";
    return 0;
}