//
//  RATIO.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/09.
//

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("RATIO.txt");

const long long MAX = 2000000000;

// game 횟수 중 win 했을 때 승률 리턴
long long Ratio(long long game, long long win){
    return (win*100)/game;
}
// 승률 1프로를 올리기 위한 최소한 연승 수
long long winStraight(long long play, long long win){
    long long lo = -1, hi = MAX;
    long long now_winRates = Ratio(play, win);
    for(int it= 0; it<100; it++){
        long long mid = (lo+hi)/2;
        long long later_winRates = Ratio(play+mid, win+mid);
        if(now_winRates<later_winRates){
            hi = mid;
        }
        else{
            lo = mid;
        }
    }
    if(hi == MAX) hi = -1; // 승률이 안오를때.. 답이없을때
    return hi;
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        long long N , M; // N -> 플레이 횟수, M -> 승리횟수
        fin >> N >> M;
        cout << winStraight(N, M) << endl;
    }
}
