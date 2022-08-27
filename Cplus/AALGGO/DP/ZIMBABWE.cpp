//
//  ZIMBABWE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/12.
//
//  1. 새 계란 가격 e에 포함된 숫자들을 재배열한 결과여야 한다.
//  2. 새 계란 가격 e보다 작아야 한다.
//  3. m으로 나누어 떨어져야 한다.
//

#include <iostream>
#include <cstring> // memset
#include <fstream>
#include <string> // string
#include <bitset> // bit mask
#include <algorithm> // sort
using namespace std;

ifstream fin("ZIMBABWE.txt");
const int MOD = 1000000007;
string e, digits; // digits : e의 자릿수들을 정렬한 것
int n; // 자릿수
int m; // m으로 나누어 떨어져야함.
//자릿수가 최대 14자리이므로 1<<14, M<=20, 그리고 egg보다 작은지 여부
int cache[1<<14][20][2];

// 과거 가격을 앞 자리부터 채워나가고 있다.
// index : 이번에 채울 자리의 인덱스
// taken : 지금까지 사용한 자릿수들의 집합
// mod   : 지금까지 만든 가격의 m에 대한 나머지
// less  : 지금까지 만든 가격이 이미 e보다 작으면 1, 아니면 0
int price(int index, int taken, int mod, int less){
    // 기저 사례 index가 자릿수
    if(index == n)
        return (less && mod == 0) ? 1 : 0; // 나머지가 0이고 가격이 e보다 작으면 1 리턴
    int& ret = cache[taken][mod][less];
    if(ret!= -1) return ret;
    ret = 0;
    for(int next = 0; next < n; next++){
        if((taken & (1<<next)) == 0){ // 과거에 사용되지 않았다면.
            //과거 가격은 새 가격보다 항상 작아야만 한다.
            if(!less && e[index] < digits[next]) // 첫자리 숫자로 크기 비교. 다음것이 크면 패쓰
                continue;
            //같은 숫자는 한 번만 선택해야 한다.
            if(next > 0 && digits[next-1] == digits[next] &&(taken & (1<<(next-1)))==0)
                continue;
            int nextTaken = taken | (1<<next); // 비트마스킹
            int nextMod = (mod * 10 + digits[next] - '0') % m; // m으로 나눈 나머지.
            int nextLess = less || e[index] > digits[next];
            ret += price(index+1, nextTaken, nextMod, nextLess);
            ret %= MOD;
        }
        
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    for(int i = 0; i < test_case; i++){
        fin >> e >> m;
        digits = e;
        sort(digits.begin(), digits.end());
        n = e.size();
        memset(cache, -1, sizeof(cache));
        cout << price(0,0,0,0) << endl;
    }
    
    return 0;
}

// 모든 경우의수를 출력.
// 1. 없거나
// 2. 이번 자릿수랑 다르거나
// 3. 이미 사용되었거나.
/*
int n;
void generate(string price, bool taken[15]){
    if(price.size() == n){
        if(price < e)
            cout << price << endl;
        return;
    }
    for(int i=0; i<n; i++){
        if(!taken[i] && (i==0 || digits[i-1] != digits[i] || taken[i-1])){
            taken[i] = true;
            generate(price + digits[i] , taken);
            taken[i] = false;
        }
    }
}
*/
