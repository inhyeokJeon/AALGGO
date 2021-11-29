//
//  PASS486.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/11.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
ifstream fin("PASS486.txt");
// brute force 로 문제해결
void brute_force();
const int MAX = 10000000;
int n, lo, hi;
int minFactor[MAX+1];
int minFactorPower[MAX+1];
int factors[MAX+1];
// 소인수 분해를 통해 약수의 개수를 구하는 공식을 이용하자
// ex) 100 = 2^2 + 5^2 -> (위의 지수들+1) 를 모두 곱해준다 -> 3 *. 3 = 9개
void getMinfactor(){
    minFactor[0] = -1;
    minFactor[1] = -1;
    for(int i=2; i<MAX+1; i++){
        minFactor[i] = i;
    }
    // root(MAX) 만큼 순회한다.
    for(int i=2; i<=int(sqrt(MAX)); i++){
        if(minFactor[i] == i)
            // i^2 부터 순회한다.
            for(int j=i*i; j<=MAX; j+=i)
                if(minFactor[j]==j) minFactor[j] = i;
    }
}

void solve(){
    factors[1] = 1;
    for(int i=2; i<=MAX;i++){
        // 소수이면
        if(minFactor[i] == i){
            factors[i] = 2;
            minFactorPower[i] = 1;
        }
        else{
            int min_prime = minFactor[i];
            int divisor = i / min_prime;
            // 더이상 min_prime 으로 나누어 떨어지지 않을때
            if(min_prime != minFactor[divisor]){
                minFactorPower[i] = 1;
            }
            // 더 나누어 질 경우
            else{
                minFactorPower[i] = minFactorPower[divisor] + 1;
            }
            int exponentNum = minFactorPower[i];
            factors[i] = (factors[divisor] / exponentNum) * (exponentNum + 1);
        }
    }
}

int main(){
    int test_case;
    fin >> test_case;
    getMinfactor();
    solve();
    //brute_force();
    for(int test=0; test < test_case; test++){
        //int n, lo, hi;
        fin >> n >> lo >> hi;
        // solve(); 시간초과
        int count= 0;
        for(int i=lo; i<hi+1; i++){
            if(factors[i] == n)
                count++;
        }
        cout << count << endl;
    }
}
// 부르트 포스!
void brute_force(){
    memset(factors,0,sizeof(factors));
    for(int i=1; i < MAX+1 ; i++){
        for(int j=i; j < MAX+1;j+=i)
            factors[j]++;
                    
    }
}

