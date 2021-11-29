//
//  1978.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/13.
//

#include <iostream>
#include <cmath>
using namespace std;

bool arr[1001];
void prime_arr(){
    int size = int(sqrt(1000));
    for(int i=2; i<size; i++){
        if(arr[i]){
            int n = i;
            while(i*n<1001){
                arr[i*n]=false;
                n++;
            }
        }
    }
}

int main(){
    int n;
    cin >> n;
    int count =0;
    for(int i=0; i<1001; i++){
        arr[i] = true;
    }
    arr[0] = false;
    arr[1] = false;
    
    prime_arr();
    for(int i=0; i<n; i++){
        int temp;
        cin >> temp;
        if(arr[temp]){
            count++;
        }
    }
    
    cout << count;
    
    
}
