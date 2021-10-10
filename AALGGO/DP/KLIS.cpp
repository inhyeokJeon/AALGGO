//
//  KLIS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/10.
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;
ifstream fin("KLIS.txt");

const int MAX = 2000000000 + 1;
int n; // 수열에 포함된 원소의 수;
int k; // k 번째
int cacheLen[501], cacheCnt[501], S[500];

int LIS(int start){
    int &ret = cacheLen[start+1];
    if(ret != -1) return ret;
    ret = 1;
    for(int next = start + 1; next < n; ++next){
        if(start == -1 ||S[start] < S[next])
            ret = max(ret, LIS(next) + 1);
    }
    return ret;
}
int count(int start){
    //기저 사례 : 길이가 1인 경우
    if(LIS(start) == 1) return 1;
    int &ret = cacheCnt[start+1];
    if(ret != -1) return ret;
    ret = 0;
    for(int next = start + 1; next < n; next++)
        if((start == -1 || S[start] < S[next]) && LIS(start) == LIS(next) + 1 )
            ret = min<long long>(MAX, (long long)ret + count(next));
    
    return ret;
}
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    for(int i = 0; i < test_case; i++){
        fin >> n >> k;
        memset(cacheLen, -1, sizeof(cacheLen));
        memset(cacheCnt, -1, sizeof(cacheCnt));
        for( int j =0; j< n; j++){
            fin >> S[j];
        }
        cout << LIS(-1) -1 << endl;
        //cout << count(0) << endl;
    }
    
    return 0;
}
