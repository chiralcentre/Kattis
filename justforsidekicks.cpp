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
    int m = (int)f.size();                     
    ft.assign(m + 1, 0);
    for (int i = 1; i < m + 1; ++i) {               
      ft[i] += f[i - 1];                             
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

typedef vector<FenwickTree> vft;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N,Q; cin >> N >> Q;
    vll values(6,0);
    for (int i = 0; i < 6; i++) cin >> values[i];
    string s; cin >> s;
    vi gems;
    for (int i = 0; i < N; i++) gems.push_back(s[i] - '0' - 1);
    // construct frequency array for every gem type in O(N) time
    vector<vll> arr(6,vll(N,0));
    for (int i = 0; i < N; i++) arr[gems[i]][i] = 1;
    /*
    cout << "test" << "\n";
    for (vll v: arr) {
      for (ll p: v) cout << p << " ";
      cout << "\n";
    } */
    // construct 6 Fenwick trees, one for each gem type
    vft trees;
    for (int i = 0; i < 6; i++) trees.push_back(FenwickTree(arr[i]));
    while (Q--) {
        int q,a,b; cin >> q >> a >> b;
        a--; b--;
        if (q == 1) {
            trees[gems[a]].update(a + 1, -1);
            trees[b].update(a + 1, 1);
            gems[a] = b;
        } else if (q == 2) {
            values[a] = b + 1;
        } else {
            vll cf(6,0);
            for (int i = 0; i < 6; i++) cf[i] = trees[i].rsq(a + 1, b + 1);
            ll sum = 0;
            for (int i = 0; i < 6; i++) sum += (values[i] * cf[i]);
            cout << sum << "\n";
        }
    }
    return 0;
}
