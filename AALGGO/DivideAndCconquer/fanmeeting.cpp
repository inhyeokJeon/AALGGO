//
//  fanmeeting.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/06.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("fan_meeting.txt");

vector<int> multiply(const vector<int> &a, const vector<int> &b){
    vector<int> c(a.size() + b.size() + 1, 0);
    for (int i = 0; i < a.size(); i++)
        for (int j = 0; j < b.size(); j++)
            c[i + j] += (a[i] * b[j]);
    return c;
}

//a += b*(10^k)
void addTo(vector<int> &a, const vector<int> &b, int k){
    a.resize(max(a.size(), b.size() + k));
    for (int i = 0; i < b.size(); i++)
        a[i + k] += b[i];
}
//a -= b
void subFrom(vector<int> &a, const vector<int> &b){
    a.resize(max(a.size(), b.size()) + 1);
    for (int i = 0; i < b.size(); i++)
        a[i] -= b[i];
}

vector<int> karatsuba(const vector<int> &a, const vector<int> &b){
    int an = a.size();
    int bn = b.size();
    if (an < bn)
        return karatsuba(b, a);
    if (an == 0 || bn == 0)
        return vector<int>();
    //크기가 작은경우 카라츠바 알고리즘을 사용하지 않고 구한다.
    if (an <= 50)
        return multiply(a, b);
/*카라츠바 알고리즘
    ∴ z0 + ( z1 * 10^half ) + ( z2 * 10^(half*2) )
        z0 = a0 * b0
        z2 = a1 * b1
        z1 = (a0 + b1) * (b0 + b1) - z0 - z2
        a0 = a 앞부분 절반 b0 = b 앞부분 절반
        a1 = a 뒷부분 절반 b1 = b 뒷부분 절반
    */
    //a와 b를 절반으로 나눈다.
    int half = an / 2;
    vector<int> a0(a.begin(), a.begin() + half);
    vector<int> a1(a.begin() + half, a.end());
    vector<int> b0(b.begin(), b.begin() + min<int>(bn, half));
    vector<int> b1(b.begin() + min<int>(bn, half), b.end());
    vector<int> z2 = karatsuba(a1, b1);
    vector<int> z0 = karatsuba(a0, b0);
    addTo(a0, a1, 0);
    addTo(b0, b1, 0);
    vector<int> z1 = karatsuba(a0, b0);
    subFrom(z1, z0);
    subFrom(z1, z2);
    vector<int> res;
    addTo(res, z0, 0);
    addTo(res, z1, half);
    addTo(res, z2, half * 2);
    return res;
}

int hugs(const string& members, const string& fans){
    int N = members.size();
    int M = fans.size();
    vector<int> a(N) , b(M);
    for(int i=0; i<N; i++){
        a[i] = (members[i] =='M');
    }
    for(int i=0; i<M; i++){
        b[M-i-1] = (fans[i] =='M');
    }
    vector<int> vec = karatsuba(a,b);
    int result =0;
    for(int i = N-1; i<M; i++){
        if(vec[i] == 0) result++;
    }
    return result;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        string members, fans;
        fin >> members;
        fin >> fans;
        cout << hugs(members, fans) << endl;
    }
    return 0;
}
