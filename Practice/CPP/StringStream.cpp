#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str1) {
    str1.push_back(',');
    stringstream output;
    output.str(str1);
    int l; 
    char ch;
    vector<int> result;
    while(output>>l>>ch){
        result.push_back(l);
    }
    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
