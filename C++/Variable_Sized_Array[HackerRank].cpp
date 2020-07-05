#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n,q,elements,t,p,r;
    cin >> n >> q;
     vector<int> a[n];
     for(int i =0;i<n;i++){
         cin >> elements;
         for(int j=0;j<elements;j++){
             cin >>t;
             a[i].push_back(t);
         }
     }
     for(int i=0;i<q;i++){
         cin >> p >>r ;
         cout<<a[p][r]<<endl;
     }
    return 0;
}
