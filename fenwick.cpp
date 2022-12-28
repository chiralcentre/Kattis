#include <bits/stdc++.h>
using namespace std;

#define LSOne(S) ((S) & -(S))                    

typedef long long ll;                            
typedef vector<ll> vll;
typedef vector<int> vi;

class FenwickTree {                              // index 0 is not used
private:
  vll ft;                                        
public:
  FenwickTree(int m) {ft.assign(m + 1, 0);}      

  void build(const vll &f) {
    int m = (int)f.size()-1;                     
    ft.assign(m + 1, 0);
    for (int i = 1; i <= m; ++i) {               
      ft[i] += f[i];                             
      if (i + LSOne(i) <= m)                       
        ft[i + LSOne(i)] += ft[i];                 
    }
  }

  FenwickTree(const vll &f) {build(f);}        

  FenwickTree(int m, const vi &s) {              
    vll f(m + 1, 0);
    for (int i = 0; i < (int)s.size(); ++i) ++f[s[i]];                                 
    build(f);                                    
  }

  ll rsq(int j) {                                
    ll sum = 0;
    for (; j; j -= LSOne(j))
      sum += ft[j];
    return sum;
  }

  ll rsq(int i, int j) { return rsq(j) - rsq(i-1); } 

  // updates value of the i-th element by v (v can be +ve/inc or -ve/dec)
  void update(int i, ll v) {
    for (; i < (int)ft.size(); i += LSOne(i))
      ft[i] += v;
  }

  int select(ll k) {                            
    int p = 1;
    while (p*2 < (int)ft.size()) p *= 2;
    int i = 0;
    while (p) {
      if (k > ft[i+p]) {
        k -= ft[i+p];
        i += p;
      }
      p /= 2;
    }
    return i+1;
  }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,Q; cin >> N >> Q;
    FenwickTree ft(N);
    while (Q--) {
        char c; int i; cin >> c >> i;
        if (c == '+') {
            int d; cin >> d;
            ft.update(i + 1, d); //add 1 since Fenwick Tree is 1 indexed
        } else cout << ft.rsq(i) << "\n";
    }
    return 0;
}
