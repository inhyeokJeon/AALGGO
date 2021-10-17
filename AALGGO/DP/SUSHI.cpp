//
//  SUSHI.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/13.
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

ifstream fin("SUSHI.txt");
int N; // 초밥의 종류
int M; // 운영진들의 예산
int cache[201]; // 최대 20000원의 가격을 100으로 나누면 200 가지 +1
vector<pair<int,int>> menu; // first -> 가격 second -> 선호도
int SUSHI(){
    int ret = 0;
    cache[0] = 0;
    for(int budget=1;  budget <=M; budget++){
        int cand = 0;
        for(int dish =0; dish<N; dish++){
            if(budget >= menu[dish].first){
                cand = max(cand, cache[(budget-menu[dish].first)%201] + menu[dish].second);
            }
        }
        cache[budget%201] = cand;
        ret = max(ret, cand);
    }
    return ret;
}
/*
 메모이제이션 동적 계획법 알고리즘
int cache[MAX_BUDGET+1];
int SUSHI(int budget){
    // 기저사례
    if(budget < 0) return 0;
    int &ret = cache[budget];
    if(ret!=-1) return ret;
    ret = 0;
    for(int i=0; i<N; i++){
        if(budget < menu[i].first) continue;
        ret = max(ret, SUSHI(budget-menu[i].first) + menu[i].second);
    }
    return ret;
}
*/
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int i = 0; i < test_case; i++){
        fin >> N >> M;
        M = M/100;
        memset(cache, -1, sizeof(cache));
        int price;
        int preference;
        menu.clear();
        for(int j=0; j<N; j++){
            fin >> price >> preference;
            price /= 100;
            menu.push_back(make_pair(price,preference));
        }
        cout << SUSHI() << endl;
        
    }
    return 0;
}
