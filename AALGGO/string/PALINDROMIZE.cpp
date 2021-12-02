//
//  PALINDROMIZE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/12/02.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("PALINDROMIZE.txt");

/*
N에서 자기 자신을 찾으면서 나타나는 부분일치를 이용해
p[]를 구한다.
p[i] = N[..i]의 접미사도 되고, 접두사도 되는 문자열의 최대 길이
*/
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
// 두 문자열이주어질때 오버랩이 되는 최대 문자의 수.
int maxOverlap(const string& original, const string& reverse){
    int n = original.size(), m = reverse.size();
    vector<int> pi = getPartialMatch(reverse);
    int begin = 0, matched= 0;
    while(begin<n){
        // 거꾸로한거랑 원래 문자열이 같다면
        if( matched<m && (original[begin+matched] == reverse[matched])){
            matched++;
            // 기저사례 n까지 도달했을때
            if(begin+matched == n){
                return matched;
            }
        }
        // 다르면
        else{
            // matched 한게 0 이면 시작점 증가.
            if(matched == 0){
                begin++;
            }
            // matched - pi[matched-1] 까지 돌아가 다시 시작한다.
            else{
                begin += matched - pi[matched-1];
                matched = pi[matched-1];
            }
        }
    }
    return 0;
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        string input;
        string reverse;
        fin >> input;
        for(int i=0; i<input.size(); i++){
             reverse += input[input.size() - i -1 ];
        }
        cout << input.size() + reverse.size() - maxOverlap(input,reverse) << endl;
    }
}
