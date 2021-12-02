//
//  BRACKETS2.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/29.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <stack>

using namespace std;
ifstream fin("BRACKETS2.txt");

bool wellMatched(const string& S){
    // 여는 괄호와 닫는 괄호를 사전에 저장해줌
    const string opening("({["), closing(")}]");
    // 이미 열린 괄호들을 저장하는 스택
    stack<char> openStack;
    for(int i=0; i<S.size(); i++){
        // 여는 괄호라면 스택에 저장한다.
        if(opening.find(S[i]) != -1) openStack.push(S[i]);
        // 아니라면 문자와 맞쳐본다.
        else{
            // 만약 비었으면 불가능
            if(openStack.empty()) return false;
            // 서로 짝이 맞지 않아도 불가능
            if(opening.find(openStack.top()) != closing.find(S[i])) return false;
            // 서로 짝이 맞다면 스택에서 제거
            openStack.pop();
        }
    }
    // 스택이 모두 비어야 성공.
    return openStack.empty();
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        string S;
        fin >> S;
        if(wellMatched(S)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}
