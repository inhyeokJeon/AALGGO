//
//  ITES.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/30.
//


#include <iostream>
#include <fstream>
#include <queue>

using namespace std;
ifstream fin("ITES.txt");
const int MOD = 10000;

// 신호 생성기
struct RNG
{
    unsigned seed;
    RNG() : seed(1983) {}//생성자
    unsigned next()
    {
         unsigned result = seed;
         seed = ((seed * 214013u) + 2531011u);
         return result % MOD + 1;
    }
};

int countRange(int k, int n){
    RNG rng; // 신호값을 생성하는 난수 생성기
    queue<int> range; // 현재 구간에 들어 있는 숫자들을 저장하는 큐
    int ret = 0, rangeSum = 0;
    for(int i=0; i<n; i++){
        // 새신호를 받아온다
        int newSignal = rng.next();
        rangeSum += newSignal;
        range.push(newSignal);
        while(rangeSum > k){
            rangeSum -= range.front();
            range.pop();
        }
        if(rangeSum == k) ret++;
    }
    return ret;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        int K, N;
        fin >> K >> N;
        cout << countRange(K,N) << endl;
    }
}
