//
//  MINASTIRITH.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/20.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>
using namespace std;

ifstream fin("MINASTIRITH.txt");
int N; // 초소 개수
const double pi = 2.0 * acos(0);  // acos(0) -> pi/2;
double x[100];
double y[100];
double r[100];
pair<double, double> ranges[100];
const int INF = 987654321;
int solveLinear(double begin, double end){
    int used =0 , idx =0;
    // 덮지 못한 선분이 남아 있는 동안 계속 함.
    while(begin < end){
        double maxCover = -1;
        // begin 을 포함 하는 것중 가장 긴 것을 선택.
        while(idx < N && ranges[idx].first <= begin){
            maxCover = max(maxCover, ranges[idx].second);
            idx++;
        }
        
        if(maxCover <= begin) return INF;
        begin = maxCover;
        used++;
    }
    return used;
}

int solveCircular(){
    int ret = INF; // 엄청 큰 값 시작으로 대입.
    for(int i=0; i<N; i++){
        if(ranges[i].first <= 0 || ranges[i].second >= 2*pi){
            // 0 을 덮는 구간을 선택
            double begin = fmod(ranges[i].second, 2*pi);
            double end = fmod(ranges[i].first+2*pi, 2*pi);
            // [begin, end] 를 덮는 구간을 구한다.
            ret = min(ret, 1+ solveLinear(begin,end));
        }
    }
    return ret;
}

void convertToRange(){
    for(int i=0; i< N; i++){
        double loc = fmod(2*pi + atan2(y[i], x[i]), 2*pi); // [0,2pi] 구간으로 변경
        double range = 2.0 * asin(r[i]/16.0);
        ranges[i] = make_pair(loc-range, loc+range);
    }
    sort(ranges, ranges+N);
    
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    for(int Test = 0; Test < test_case; Test++){
        fin >> N;
        for(int i =0 ; i< N; i++){
            fin >> y[i] >> x[i] >> r[i];
        }
        convertToRange();
        if(solveCircular() == INF){
            cout << "IMPOSSIBLE" << endl;
        }
        else cout << solveCircular() << endl;
    }
    return 0;
}
