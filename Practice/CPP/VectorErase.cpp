#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    vector<int> v;
    cin>>n;
    for(int i=0;i<n;i++){
        int num;
        cin >> num;
        v.push_back(num);
    }
    int x;
    cin>>x;
    v.erase(v.begin()+x-1);
    int a,b;
    cin>>a>>b;
    v.erase(v.begin()+a-1,v.begin()+b-1);
    int s = v.size();
    cout<<s<<endl;
    for(int j=0;j<s;j++){
        cout<<v[j]<<" ";
    }
    return 0;
}
