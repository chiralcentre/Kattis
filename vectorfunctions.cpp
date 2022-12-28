#include "vectorfunctions.h"

using namespace std;

void backwards(vector<int>& vec){
    for (int i = 0; i < vec.size() / 2; i++){
        int temp = vec[i];
        vec[i] = vec[vec.size() - i - 1];
        vec[vec.size() - i - 1] = temp;
    }
}

vector<int> everyOther(const vector<int>& vec){
    vector<int> ans;
    for (int i = 0; i < vec.size(); i += 2) {
        ans.push_back(vec[i]);
    }
    return ans;
}

int smallest(const vector<int>& vec){
    int ans = 10000;
    for (int n : vec) ans = min(n, ans);
    return ans;
}

int sum(const vector<int>& vec){
    int ans = 0;
    for (int n : vec) ans += n;
    return ans;
}

int veryOdd(const vector<int>& suchVector){
    int ans = 0;
    for (int i = 1; i < suchVector.size(); i += 2) {
        if (suchVector[i] % 2 == 1) ans++;
    }
    return ans;
}
