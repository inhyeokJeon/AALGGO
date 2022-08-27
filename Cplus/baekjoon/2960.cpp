//
//  2960.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/13.
//

#include <iostream>
#include <vector>

using namespace std;



int main(){
    int n,k;
    cin >> n >> k;
    vector<bool> vec(n+1, true);
    vec[0] = false;
    vec[1] = false;
    int count = 0;
    for(int i=2; i<n+1 ; i++){
        if(vec[i]){
            for(int j=i; j< n+1;j+=i)
                if(vec[j]){
                    vec[j] = false;
                    count++;
                    if(count == k){
                        cout << j;
                        return 0;
                    }
                }
        }
    }
    return 0;
}

