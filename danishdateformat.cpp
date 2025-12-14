#include <bits/stdc++.h>

using namespace std;

int y,m,d;

unordered_map<int, string> monthToDanish = {
    {1,  "januar"},
    {2,  "februar"},
    {3,  "marts"},
    {4,  "april"},
    {5,  "maj"},
    {6,  "juni"},
    {7,  "juli"},
    {8,  "august"},
    {9,  "september"},
    {10, "oktober"},
    {11, "november"},
    {12, "december"}
};

int main() {
    scanf("%d/%d/%d",&m,&d,&y);
    printf("%d. %s %d\n",d,monthToDanish[m].c_str(),y);
    return 0;
}