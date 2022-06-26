#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> books;
    for (int i = 0; i < N; i++) {
        int x; cin >> x; books.push_back(x);
    }
    sort(books.begin(),books.end(), greater<>());
    long long sum = 0;
    for (int i = 0; i < N; i++){
        if (i%3 != 2) sum += books[i];
    }
    cout << sum;
    return 0;
}