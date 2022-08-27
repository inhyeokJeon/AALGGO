//
//  NUMB3RS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/29.
//

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

ifstream fin("NUMB3RS.txt");

int n=0; // 마을의 수
int d=0; // 지난 일수
int p=0; // 교도소가 있는 마을의 번호
int q=0; // 계산할 마을의 번호
double cache[51][101]; // 메모이제이션을 위해
int A[51][51];
int deg[51];

/*
마을과 인접해 있는 마을의 수를 계산하여 deg에 저장.
 */
void Calculate_deg(int n){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(A[i][j])
                deg[i]++;
        }
    }
}
/*
역으로 생각해보자 -> d일 후 q마을 부터 시작.
here -> 현재 위치
days -> 지난 일 수.
 */
double dunibal(int here, int days){
    // 기저 사례
    if(days==0) return (here== p ? 1.0 : 0.0);
    double &ret = cache[here][days];
    if(ret > -0.5) return ret;
    ret = 0.0;
    for(int there = 0; there < n; there++){
        if(A[here][there])
            ret += dunibal(there, days-1) / deg[there];
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    for (int i=0; i < Test_case ; i++){
        fin >> n;
        fin >> d;
        fin >> p;
        memset(cache,-1,sizeof(cache));
        memset(deg,0,sizeof(deg));
        memset(A,0,sizeof(A));
        for(int j =0; j< n; j++){
            for(int k=0; k<n; k++){
                fin >> A[j][k];
            }
        }
        Calculate_deg(n);
        int t=0; // 확률을 계산할 마을 번호의 수
        fin >> t;
        for(int j=0; j<t; j++){
            fin >> q;
            printf("%.8f ", dunibal(q,d));
        }
        cout << endl;
    }
    return 0;
}
