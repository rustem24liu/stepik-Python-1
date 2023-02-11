#include <bits/stdc++.h>
using namespace std;
int main (){
    int n;
    cin >> n;
    int arr[n][n];
    for (int i = 0; i < n; i++){
        cout << i << " ";
        for (int j = 1; j < n;j++){
            if(i*j==0){
                cout << j << " ";
            }

            else {
            cout << (i) * (j) << " ";
            }

        }
        cout << endl;
        
    }
    
    
}