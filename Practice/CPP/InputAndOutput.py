#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    float a,b,c,z;
    cin>>a>>b>>c;
    if(0<a<1000 && 0<b<1000 && 0<c<1000)
        cout<<(a+b+c);
    else
        cout<<"Not in range";
    return 0;
}
