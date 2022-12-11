#include <algorithm>
#include <iostream>
#include <vector>
#include <tuple>
#include <cmath>

using namespace std;

typedef tuple<int,int,int> iii;
typedef pair<double,int> di;
typedef vector<di> vdi;
typedef vector<iii> viii;
// use 1 billion to represent infinity
const int INF = 1e9;

double distance(iii p1, iii p2) {
    int x1 = get<0>(p1), y1 = get<1>(p1), z1 = get<2>(p1);
    int x2 = get<0>(p2), y2 = get<1>(p2), z2 = get<2>(p2); 
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2));
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    viii points;
    for (int i = 0; i < N; i++) {
        int x,y,z;
        cin >> x >> y >> z;
        points.push_back(make_tuple(x,y,z));
    }
    //Prim's variant for dense graphs is used
    vector<bool> taken(N,false);
    vdi A;
    for (int i = 0; i < N; i++) A.push_back(make_pair(INF,i));
    A[0] = make_pair(0,0);  //start from first point
    taken[0] = true;
    double cost = 0; int counter = 1;
    while (counter < N) {
        int lowest = INF, v = 0; //scan A to get v where A[v][0] is minimum in A
        for (int i = 0; i < N; i++) {
            if (A[i].first < lowest) {
                lowest = A[i].first;
                v = i;
            }
        }
        //add vertices to taken
        if (!taken[v]) {
            taken[v] = true;
            counter++;
        }
        if (!taken[A[v].second]) {
            taken[A[v].second] = true;
            counter++;
        }
        cost = max(cost, A[v].first); //find maximin cost
        A[v] = make_pair(INF,A[v].second); // prevent picking same point again
        for (int i = 0; i < N; i++) {
            if (!taken[i]) {
                double d =  distance(points[i],points[v]);
                if (A[i].first > d) A[i] = make_pair(d,v);
            }
        }
    }
    cout << ceil(cost) << endl;
    return 0;
}