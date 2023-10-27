#include <bits/stdc++.h>
#include <set>
#include <deque>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

char instr[16];
int N; ll X,Y,Z; 

// comparator which sorts in ascending order for first element and descending order for second element
bool sortByCond(const pll &a, const pll &b) {
    if (a.first != b.first) return a.first < b.first;
    return a.second > b.second;
}
 
int main() {
    scanf("%d",&N);
    deque<pll> cards;
    set<pll, decltype(&sortByCond)> freqToCard(&sortByCond);
    unordered_map<ll,ll> cardToFreq;
    while (N--) {
        scanf("%s",instr);
        if (instr[0] == 'P') {
            scanf("%lld %lld",&X,&Y);
            (instr[4] == 'T') ? cards.push_front({X,Y}) : cards.push_back({X,Y});
            ll count = cardToFreq[Y];
            cardToFreq[Y] = X + count;
            // exception is not thrown if pair is not present
            freqToCard.erase({count, Y});
            freqToCard.insert({count + X, Y});
        } else {
            scanf("%lld", &Z);
            while (Z > 0) {
                pll p = (instr[7] == 'T') ? cards.front() : cards.back();
                (instr[7] == 'T') ? cards.pop_front() : cards.pop_back();
                ll freq = p.first, label = p.second;
                ll used = min(Z, freq);
                Z = max(Z - freq, 0ll);
                if (used < freq) {(instr[7] == 'T') ? cards.push_front({freq - used, label}) : cards.push_back({freq - used, label});}
                ll count = cardToFreq[label];
                cardToFreq[label] = count - used;
                freqToCard.erase({count, label});
                freqToCard.insert({count - used, label});
            }
        }
        printf("%lld\n", (*freqToCard.rbegin()).second);
    }
    return 0;
}