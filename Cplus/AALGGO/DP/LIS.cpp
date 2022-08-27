//
//  LIS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/15.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstring>

using namespace std;

ifstream fin("LIS.txt");
int cache[501];
int sequence[501];
int num;
int LIS(int a){
    int &ret = cache[a+1];
    if(ret != -1) return ret;
    ret = 1;
    for(int i = a + 1; i < num; ++i){
        if(a == -1 ||sequence[a] < sequence[i])
            ret = max(ret, LIS(i) + 1);
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        fin >> num;
        vector<int> list;
        memset(cache,-1,sizeof(cache));
        memset(sequence,-1,sizeof(sequence));
        for(int j=0; j< num; j++){
            fin >> sequence[j];
        }
        cout << LIS(-1)-1 << endl;
    }
    return 0;
}

