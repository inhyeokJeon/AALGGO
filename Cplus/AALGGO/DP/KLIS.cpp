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

void reconstruct(int start, int skip, vector<int>& result){
    // 1. S[start]는 항상 LIS에 포함된다.
    if(start!=-1) result.push_back(S[start]);

    // 2. 뒤에 올 수 있는 숫자들과 위치의 목록을 만든다. pair사용
    vector<pair<int,int>> followers;
    for(int next = start +1; next<n; next++){
        if((start == -1 || S[start] < S[next]) && LIS(start) == LIS(next) + 1 )
            followers.push_back(make_pair(S[next],next));
    }
    sort(followers.begin(), followers.end());
    // 3. k번째 LIS의 다음 숫자를 찾는다.
    for(int i=0; i< followers.size(); i++){
        // 이 숫자를 뒤에 이어서 만들 수 있는 LIS의 개수를 본다.
        int index = followers[i].second;
        int cnt = count(index);
        if( cnt <= skip) skip -= cnt;
        else{
            //다음 숫자는 S[index] 임을 알았다.
            //4. 재귀호출을 통해
            reconstruct(index, skip, result);
            break;
        }
    }
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
        vector<int> result;
        reconstruct(-1,k-1,result);
        for(int j=0; j<result.size(); j++){
            cout << result[j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
