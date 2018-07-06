#include <bits/stdc++.h>

using namespace std;

int solvea(int a1, int a2, int a3, int b1, int b2, int b3){
    int totala=0;
    if (a1>b1)
        totala=totala+1;
    if(a2>b2)
        totala=totala+1;
    if(a3>b3)
        totala=totala+1;
    return totala;
          
}
int solveb(int a1, int a2, int a3, int b1, int b2, int b3){
    int totalb=0;
    if (b1>a1)
        totalb=totalb+1;
    if(b2>a2)
        totalb=totalb+1;
    if(b3>a3)
        totalb=totalb+1;
    return totalb;
          
}

int main() {
    int a,b, a0;
    int a1;
    int a2;
    cin >> a0 >> a1 >> a2;
    int b0;
    int b1;
    int b2;
    cin >> b0 >> b1 >> b2;
    a = solvea(a0, a1, a2, b0, b1, b2);
    b = solveb(a0, a1, a2, b0, b1, b2);
    cout<<a<<" "<<b;
    return 0;
}
