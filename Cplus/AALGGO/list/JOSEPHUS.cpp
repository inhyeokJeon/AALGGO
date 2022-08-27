//
//  JOSEPHUS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/28.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>

using namespace std;
ifstream fin("JOSEPHUS.txt");

void josephus(int N, int K){
    list<int> survivors;
    for(int i=1; i<=N; i++){
        survivors.push_back(i);
    }
    // 죽을사람의 포인터 ㅜㅜ
    list<int>::iterator kill = survivors.begin();
    while(N>2){
        // erase 는 kill사람을 없애고 다음 사람을 포인터로 가르킨다.
        kill = survivors.erase(kill);
        N--;
        // 끝에가면 다시 첨으로 돌아감.
        if(kill == survivors.end()) kill = survivors.begin();
        // k번 다음사람을 가르킨다.
        for(int i=0; i< K-1; i++) {
            kill++;
            // 끝에가면 다시 첨으로 돌아감.
            if(kill == survivors.end()) kill = survivors.begin();
        }
    }
    cout << survivors.front() << " " << survivors.back() << endl;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        int N; // 사람수
        int K; // K번째가 죽음
        fin >> N >> K;
        josephus(N,K);
    }
}
