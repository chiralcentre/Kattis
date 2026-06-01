#include <bits/stdc++.h>
using namespace std;
static const int LIMIT = 100000000;   // valid values 0 .. LIMIT-1

int main(){
    int A; long long X;
    scanf("%d %lld", &A, &X);

    char op[5]; int y[5], c[5];
    int m = 0;                                  // count of USEFUL ops
    for(int i=0;i<A;i++){
        char b[4]; int yy, cc;
        scanf("%s %d %d", b, &yy, &cc);
        if(yy == 0) continue;                   // +0/-0 are no-ops; *0 only ever yields 0 (the source)
        op[m]=b[0]; y[m]=yy; c[m]=cc; ++m;
    }

    if(X == 0){printf("0\n"); return 0;}

    vector<int> dist(LIMIT, INT_MAX);           // ~400 MB, fine under 2048 MB
    vector<int> bucket[4];

    dist[0] = 0;
    bucket[0].push_back(0);
    int answer = -1;

    for(int d=0;;d++){
        int b = d & 3;
        if(bucket[b].empty()){
            bool any=false; 
            for(int k=0;k<4;k++) if(!bucket[k].empty()){any=true;break;}
            if(!any) break;
            continue;
        }
        while(!bucket[b].empty()){
            int v = bucket[b].back(); bucket[b].pop_back();
            if(dist[v] != d) continue;
            if(v == X){ answer = d; goto done; }
            for(int i=0;i < m;i++){
                long long nv;
                switch(op[i]){
                    case '+': nv = (long long)v + y[i]; break;
                    case '-': nv = (long long)v - y[i]; break;
                    case '*': nv = (long long)v * y[i]; break;
                    default : nv = v / y[i];            break;
                }
                if(nv < 0 || nv >= LIMIT) continue;
                int ndist = d + c[i];
                if(ndist < dist[(int)nv]){
                    dist[(int)nv] = ndist;
                    bucket[ndist & 3].push_back((int)nv); // optimisation over modulus
                }
            }
        }
    }
done:
    if(answer < 0) printf("Engin leid!\n");
    else           printf("%lld\n", answer);
    return 0;
}