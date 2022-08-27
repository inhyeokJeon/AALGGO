//
//  TILING2.cpp
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

ifstream fin("TILING2.txt");
int cache[101];

int TILING2(int n){
    // 기저사례
    if(n<=1){
        return 1;
    }
    else if(n==2) return 2;
    else if(n<1) return 0;
    int &ret = cache[n];
    if(ret != -1) return ret;
    ret = 0;
    ret = ret + (TILING2(n-1) + TILING2(n-2))% 1000000007;
    
    return ret;
}


int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    int n;
    for (int i=0; i< Test_case ; i++){
        fin >> n;
        memset(cache,-1,sizeof(cache));
        cout << TILING2(n) << endl;
    }
    return 0;
}
