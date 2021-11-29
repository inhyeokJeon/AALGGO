//
//  WITHDRAWAL.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/06.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cstring>
using namespace std;

ifstream fin("WITHDRAWAL.txt");

int n; // 수강하는 과목 수
int k; // 남겨야할 최소 과목 수
int studentNum[1000]; // i번째 과목 수강생 수
int classRank[1000]; // i 번째과목 등 수

/*
 최소 누적등수(average)
 누적등수 = sum(r[i])/sum(c[i])
 누적등수가 <= average 인가 아닌가.
 0 <= sum( average*학생수[i] - 등수[i])
 */
bool decision(double average){
    // v[i] == x*r[i] - c[i]
    vector<double> v;
    double sum = 0;
    for(int i=0; i<n; i++){
        v.push_back(average*studentNum[i] - classRank[i]);
    }
    // 정렬하여 v 중 가장 큰것들을 고르기 위해
    sort(v.begin(), v.end());
    // k개 이상을 수강하는 것
    for(int i=n-k; i<n; i++){
        sum+=v[i];
    }
    return sum>=0;
}

// 확률은 0~ 1 이내의 숫자이기 떄문.
double optimize(){
    double lo=0, hi = 1;
    for(int i=0; i<100; i++){
        double mid = (lo+hi)/2.0;
        if(decision(mid)){
            hi = mid;
        }
        else{
            lo = mid;
        }
    }
    return hi;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        fin >> n >> k;
        for(int i=0; i<n; i++){
            fin >> classRank[i] >> studentNum[i];
        }
        printf("%.8f\n", optimize());
    }
    
}
