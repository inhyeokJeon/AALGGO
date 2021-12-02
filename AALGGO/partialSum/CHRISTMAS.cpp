//
//  CHRISTMAS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/27.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
ifstream fin("CHRISTMAS.txt");
int N; // 인형 상자의 개수
int K; // 어린이의 수

int firstQ(const vector<int> &boxSum){
    const int MOD = 20091101;
    int result = 0;
    //psum[]의 각 값을 몇 번이나 본 적 있는지 기록
    vector<long long> count(K, 0);
    for (int i = 0; i < boxSum.size(); i++)
        count[boxSum[i]]++;
    //두 번 이상 본 적 있다면 이 값 중 두 개를 선택하는 방법의 수를 더한다
    //count[i]개 중 2개를 고를 경우의 수
    //nC2를 더한다 (n=count[i])
    for (int i = 0; i < K; i++)
        if (count[i] >= 2)
            result = (result + ((count[i] * (count[i] - 1)) / 2)) % MOD;
    return result;
}
int secondQ(const vector<int> &boxSum){
    
    vector<int> ret(boxSum.size(),0);
    //prev[S] = boxSum[] 이 마지막 S였던 위치
    vector<int> prev(K, -1);
    for(int i=0; i<boxSum.size(); i++){
        // i번째 상자를 고려하지 않는경우
        if(i>0)
            ret[i] = ret[i-1];
        else ret[i] = 0;
        int loc = prev[boxSum[i]];
        if(loc !=-1) ret[i] = max(ret[i], ret[loc] +1);
        prev[boxSum[i]] = i;
    }
    return ret.back();
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        fin >> N >> K;
        vector<int> boxSum(N+1,0);
        vector<int> box(N,0);
        for(int i=0; i<N; i++){
            fin >>box[i];
        }
        boxSum[0] = 0;
        for(int i=1; i<N+1; i++){
            boxSum[i] = (boxSum[i-1] + box[i-1]) % K;
        }
        cout << firstQ(boxSum) << " " << secondQ(boxSum) << endl;
        boxSum.clear();
    }
}
