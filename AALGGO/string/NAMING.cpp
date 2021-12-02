//
//  NAMING.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/12/01.
//


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("NAMING.txt");

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
// s 의 접미사도 되고 접두사도 되는 문자열의 길이를 반환한다.
vector<int> getPrefixSuffix(const string& s){
    vector<int> ret, pi = getPartialMatch(s);
    int k = s.size();
    while(k>0){
        ret.push_back(k);
        k = pi[k-1];
    }
    return ret;
}
int main(){
    string father, mother;
    fin >> father  >> mother;
    string combined = father + mother;
    vector<int> ret = getPrefixSuffix(combined);
    sort(ret.begin(), ret.end());
    for(int i=0; i< ret.size(); i++){
        cout << ret[i] << " ";
    }
    /*
    vector<int> test = getPartialMatch(combined);
    for(int i=0; i<test.size(); i++){
        cout << "i: "<< i << " value : " << test[i] << endl;
    }
    */
    cout << endl;
    return 0;
}
