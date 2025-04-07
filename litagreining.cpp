#include <bits/stdc++.h>

using namespace std;

int R,G,B;

string solve(int R, int G, int B) {
    if (R > G && R > B) return "raudur";
    if (G > R && G > B) return "graenn";
    if (B > R && B > G) return "blar";
    if (R == G && B < R && B < G) return "gulur";
    if (R == B && G < R && G < B) return "fjolubleikur";
    if (G == B && R < G && R < B) return "blagraenn";
    if (R == G && G == B) {
        if (R == 0) return "svartur";
        else if (R == 255) return "hvitur";
        else return "grar";
    }
    return "othekkt";
}

int main() {
    scanf("%d %d %d",&R,&G,&B);
    printf("%s\n",solve(R,G,B).c_str());
    return 0;
}