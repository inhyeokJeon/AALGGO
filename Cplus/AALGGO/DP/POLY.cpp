//
//  POLY.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/28.
//

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

const int MOD = 10000000;
ifstream fin("POLY.txt");
int cache[101][101];
/*
n : n개의 사각형으로 이루어짐.
first : 맨 윗줄의 사각형의 수
return 폴리노미아 수
*/
int POLY(int n, int first){
    // 기저
    if(n==first) return 1;
    int &ret = cache[n][first];
    if(ret != -1) return ret;
    ret = 0;
    for(int second=1; second <= n-first ; second++){
        int add = second + first - 1;
        add *= POLY(n-first, second);
        add %= MOD;
        ret += add;
        ret %= MOD;
    }
    return ret;
}
    
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        int sum=0;
        int n=0;
        fin >> n;
        memset(cache,-1,sizeof(cache));
        for (int j = 1; j <= n; j++){
            sum += POLY(n, j);
            sum %= MOD;
        }

        cout << sum << endl;
    }
    return 0;
}
