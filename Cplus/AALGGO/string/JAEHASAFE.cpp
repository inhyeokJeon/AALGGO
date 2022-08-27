//
//  JAEHASAFE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/12/03.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("JAEHASAFE.txt");


vector<int> getPartialMatch(const string& N){
    int m = N.size();
    vector<int> pi(m,0);
    // KMP 로 자기 자신을 찾는다
    // N을 N에서 찾는다. begin = 0 이면 자기 자신을 찾아버리니깐 안됨!
    int begin =1, matched = 0;
    while(begin+matched < m){
        if(N[begin+matched] == N[matched]){
            matched++;
            pi[begin + matched-1] = matched;
        }
        else{
            if(matched == 0){
                begin++;
            }
            else {
                begin += matched - pi[matched-1];
                matched = pi[matched-1];
            }
        }
    }
    return pi;
}
// H 속에서 N이 출현하는 시작 위치를 모두 반환한다.
vector<int> kmpSearch(const string& H, const string& N){
    int n = H.size(), m = N.size();
    vector<int> ret;
    vector<int> pi = getPartialMatch(N);
    int begin = 0, matched=0;
    while(begin + m <= n){
        // 짚더미의 H의 해당 글자가 N의 해당글자가 같을때
        if(matched < m && H[begin+matched] == N[matched]){
            matched++;
            // N의 글자가 H에 포함된다면
            if(matched == m){
                ret.push_back(begin);
            }
        }
        else{
            if(matched==0) begin++;
            else{
                begin += matched - pi[matched-1];
                matched = pi[matched-1];
            }
        }
        
    }
    return ret;
}

int shifts(const string& original, const string& target){
    // original+original 속에서 target 을 포함하는 가장 짧은 위치 index->0
    return kmpSearch(original + original,target)[0];
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        int N;
        fin >> N;
        vector<string> vec(N+1);
        for(int i=0; i<N+1; i++){
            fin >> vec[i];
        }
        int count = 0;
        for(int i=0; i<N; i++){
            // 변화기 전과 후의 위치를 바꿔 찾는다.
            if( i%2 == 0){  // 시계방향
                count += shifts(vec[i+1], vec[i]);
            }
            else{ // 시계 반대방향
                count += shifts(vec[i], vec[i+1]);
            }
        }
        cout << count << endl;
    }
}

