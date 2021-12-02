//
//  HABIT.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/12/04.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
ifstream fin("HABIT.txt");

// 각 접미사들의 첫 t글자를 기준으로 한 그룹 번호가 주어질 때,
// 주어진 두 접미사를 첫 2*t글자를 기준으로 비교한다.
// group[]은 길이가 0인 접미사도 포함한다.
struct Comparator {
    const vector<int>& group;
    int t;
    Comparator(const vector<int>& _group, int _t) : group(_group), t(_t){}
    bool operator() (int a, int b){
        // 첫 t 글자가 다르면 이들을 이용해 비교한다.
        if(group[a] != group[b]) return group[a] < group[b];
        // 아니라면 첫 t글자를 비교한다.
        return group[a+t] < group[b+t];
    }
};
// 접미사 배열을 반환한다.
vector<int> getSuffixArray(const string& s){
    int n = s.size();
    // group[i] = 접미사들을 첫 r글자를 기준으로 정렬했을 때,
    // S[i..]가 들어가는 그룹의 번호
    // t = 1일 때는 정렬할 것도 없이 S[i..]의 첫 글자로 그룹 번호를
    // 정해줘도 같은 효과가 있다.
    int t=1;
    vector<int> group(n+1);
    for(int i=0; i<n; i++) group[i] = s[i];
    group[n] = -1;
    // 접미사 배열이 반환될 값
    vector<int> perm(n);
    for(int i=0; i<n; i++) perm[i] = i;
    while(t < n){
        // group[] 은 첫 t글자를 기준으로 계산해 둔다.
        // 첫 2t글자를 기준으로 perm을 다시 정렬.
        Comparator compareUsing2T(group,t);
        sort(perm.begin(), perm.end(), compareUsing2T);
        // 2t글자가 을 넘는다면 이제 접미사 배열 성공
        t *=2;
        if(t>=n) break;
        // 2t글자를 기준으로 한 그룹 정보를 만든다.
        vector<int> newGroup(n+1);
        newGroup[n] = -1;
        newGroup[perm[0]] = 0;
        for(int i=1; i<n; i++){
            if(compareUsing2T(perm[i-1], perm[i]))
                newGroup[perm[i]] = newGroup[perm[i-1]]+1;
            else
                newGroup[perm[i]] = newGroup[perm[i-1]];
        }
        group = newGroup;
    }
    return perm;
}

// 공통 접두사의 최대 길이를 리턴
int commonPrefix(const string& s, int i, int j){
    int k =0;
    while(i<s.size() && j < s.size() && s[i] == s[j]){
        i++; j++; k++;
    }
    return k;
}
int longestFrequent(int k, const string& s){
    // s 의 접미사배열
    vector<int> a = getSuffixArray(s);
    int ret =0;
    for(int i=0; i+k <= s.size(); i++){
        ret = max(ret, commonPrefix(s, a[i], a[i+k-1]));
    }
    return ret;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        int k;
        string s;
        fin >> k >> s;
        cout << longestFrequent(k, s) << endl;
    }
    
}
