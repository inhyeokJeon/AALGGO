//
//  PACKING.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/30.
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <vector>
#include <tuple>
using namespace std;

int N; // 가지고싶은 물건의 수
int W; // 캐리어의 용량
vector<tuple<string,int,int>>vec;
vector<string> answer;
int answer_count;
int answer_precious;
int cache[1001][101];

ifstream fin("PACKING.txt");
int packing(int, int);

void solve_answer(int capacity, int item){
    if(item == N) return;
    //  안담앗을때 같음.
    if(packing(capacity,item) == packing(capacity, item+1)){
        solve_answer(capacity, item+1);
    }
    else{ // 담았을때..
        answer.push_back(get<0>(vec[item]));
        answer_count++;
        answer_precious += get<2>(vec[item]);
        solve_answer(capacity - get<1>(vec[item]), item +1);
    }
}
int packing(int capacity, int item){
    // 기저 사례
    if(item == N) return 0;
    int& ret = cache[capacity][item];
    if(ret != -1) return ret;
    
    //물건 안담을 경우
    ret = packing(capacity, item +1);
    //물건 담을 경우
    if(capacity >= get<1>(vec[item])){
        ret = max(ret, packing(capacity-get<1>(vec[item]), item+1) + get<2>(vec[item]));
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    for (int i=0; i < Test_case ; i++){
        fin >> N;
        fin >> W;
        vec.clear();
        answer.clear();
        answer_count =0;
        answer_precious =0;
        memset(cache, -1, sizeof(cache));
        for(int i=0; i <N; i++){
            string str;
            int volume;
            int precious;
            fin >> str;
            fin >> volume;
            fin >> precious;
            vec.push_back(make_tuple(str,volume,precious));
        }
        solve_answer(W, 0);
        cout << answer_precious << " " << answer_count << endl;
        for(int i=0; i< answer.size(); i++){
            cout << answer[i] << endl;
        }
    }
    
    return 0;
}


