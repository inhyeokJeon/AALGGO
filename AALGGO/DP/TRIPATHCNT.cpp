//
//  TRIPATHCNT.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/28.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
int n;
ifstream fin("TRIPATHCNT.txt");
int cache[100][100];
int arr[101][101];
 
int path2(int y, int x){
    if(y == n ) return 0;
    int &ret = cache[y][x];
    if(ret != -1) return ret;
    ret = arr[y][x];
    ret = ret + max(path2(y+1,x), path2(y+1, x+1));
    return ret;
}
int countcache[101][101];
int count(int y, int x){
    if(y == n-1 ) return 1;
    int &ret = countcache[y][x];
    if(ret != -1) return ret;
    ret = 0;
    if(path2(y+1, x+1) >= path2(y+1,x) ){
        ret = ret + count(y+1,x+1);
    }
    
    if(path2(y+1, x+1) <= path2(y+1,x) ){
        ret = ret + count(y+1,x);
    }
    
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        fin >> n;
        memset(cache,-1,sizeof(cache));
        memset(arr,-1,sizeof(arr));
        memset(countcache,-1,sizeof(countcache));
        for (int j=0; j<n; j++){
            for(int k=0; k<=j; k++){
                fin >> arr[j][k];
            }
        }
        
        cout << count(0,0) << endl;
    }
    return 0;
}
