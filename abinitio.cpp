#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<bool> vb;
typedef vector<vb> vvb;

const ll MOD = 1000000007;
const int MAX = 4000;

/*
//do not declare in main to avoid stack overflow
bool inEdges[MAX][MAX]; bool outEdges[MAX][MAX]; 
bool inEdgesC[MAX][MAX]; bool outEdgesC[MAX][MAX]; */

int main() {
    //vectors are used instead of 2D arrays since swap operation does not work in O(1) time for arrays
    int V,E,Q; scanf("%d %d %d",&V,&E,&Q);
    vvb inEdges(V,vb(V,false)), outEdges(V,vb(V,false));
    vvb inEdgesC(V,vb(V,false)), outEdgesC(V,vb(V,false));
    //initialisation
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            inEdges[i][j] = false; outEdges[i][j] = false;
            if (i != j) {inEdgesC[i][j] = true; outEdgesC[i][j] = true;}
        }
    }
    //fill in edges
    for (int i = 0; i < E; i++) {
        int u,v; scanf("%d %d",&u,&v);
        inEdges[v][u] = true; outEdges[u][v] = true;
        inEdgesC[v][u] = false; outEdgesC[u][v] = false;
    }
    //handle queries
    for (int i = 0; i < Q; i++) {
        int q; scanf("%d",&q);
        if (q == 1) {
            inEdges.push_back(vb {}); outEdges.push_back(vb {});
            inEdgesC.push_back(vb {}); outEdgesC.push_back(vb {});
            for (int j = 0; j < V; j++) {
                inEdges[j].push_back(false); outEdges[j].push_back(false);
                inEdges[V].push_back(false); outEdges[V].push_back(false);
                inEdgesC[j].push_back(true); outEdgesC[j].push_back(true);
                inEdgesC[V].push_back(true); outEdgesC[V].push_back(true);
            }
            inEdges[V].push_back(false); outEdges[V].push_back(false);
            inEdgesC[V].push_back(false); outEdgesC[V].push_back(false);
            V++;
        }
        else if (q == 2) { // O(1)
            int u,v; scanf("%d %d",&u,&v);
            inEdges[v][u] = true; outEdges[u][v] = true;
            inEdgesC[v][u] = false; outEdgesC[u][v] = false;
        } else if (q == 3) { // O(V)
            int a; scanf("%d",&a);
            for (int i = 0; i < V; i++) {
                if (inEdges[a][i]) {
                    outEdges[i][a] = false; outEdgesC[i][a] = true;
                    inEdges[a][i] = false; inEdgesC[a][i] = true;
                }
                if (outEdges[a][i]) {
                    inEdges[i][a] = false; inEdgesC[i][a] = true;
                    outEdges[a][i] = false; outEdgesC[a][i] = true;
                }
            }
        } else if (q == 4) { // O(1)
            int u,v; scanf("%d %d",&u,&v);
            inEdges[v][u] = false; outEdges[u][v] = false;
            inEdgesC[v][u] = true; outEdgesC[u][v] = true;
        } else if (q == 5) { // O(1)
            swap(inEdges,outEdges);
            swap(inEdgesC,outEdgesC);
        } else { // O(1)
            swap(inEdges,inEdgesC);
            swap(outEdges,outEdgesC);
        }
    }
    //print output
    printf("%d\n",V);
    for (int i = 0; i < V; i++) {
        ll h = 0, p = 1, c = 0;
        for (int j = 0; j < V; j++) {
            if (outEdges[i][j]) {
                h += p * j; p *= 7;
                h %= MOD; p %= MOD;
                c ++;
            }
        }
        printf("%lld %lld\n",c,h);
    }
    return 0;
}