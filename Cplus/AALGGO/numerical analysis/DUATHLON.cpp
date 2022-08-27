//
//  DUATHLON.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/10.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

ifstream fin("DUATHLON2.txt");
int track; // 트랙 길이
int n; // 경쟁자 수
// <run time, cycle time> = <달리기 속도, 자전거 속도>
vector<pair<double, double> > people;
pair<double, double> fool;

// 달리기 구간이 run 일때 i 번 선수가 걸리는 시간
double time(int i, double run){
    double cycle = track - run;
    return (run / people[i].first) + (cycle / people[i].second);
}
// cheater 가 걸리는 시간
double time(double run){
    double cycle = track - run;
    return (run / fool.first + cycle / fool.second);
}

// 달리기 거리가 주어질 때 가장 빠른 사람과 cheater 의 시간 차이.
double diff(double run){
    double others = time(0, run);
    double cheater = time(run);
    for(int i=1; i<people.size(); i++){
        others = min(others, time(i,run));
    }
    return others - cheater;
}

// 차이나는 최대치 run distance 를 출력.
double solve(){
    double lo = 0, hi = track;
    for(int it= 0; it<100; it++){
        // 삼분 탐색 1/3 지점
        double oneThird = (2*lo+hi)/3;
        // 2/3 지점
        double twoThird = (lo+2*hi)/3;
        if(diff(oneThird) > diff(twoThird)){
            hi = twoThird;
        }
        else{
            lo = oneThird;
        }
    }
    return (lo+hi)/2;
}

int main(){
    while(fin>> track){
        fin >> n;
        double run, cycle;
        for(int i=0; i<n-1; i++){
            fin >> run >> cycle;
            people.push_back(make_pair(run,cycle));
        }
        fin >> run >> cycle;
        fool = make_pair(run, cycle);
        
        double runDistance = solve();
        double cycleDistance = track - runDistance;
        double timeDiff = diff(runDistance);
        if(timeDiff >= 0.0){
            const char *result = "The cheater can win by %.0f seconds with r = %0.2fkm and k = %0.2fkm.\n";
            // * 3600 -> 시간을 초로 나타낸다.
            printf(result, timeDiff*3600,runDistance, cycleDistance);
            //The cheater can win by 612 seconds with r = 14.29km and k = 85.71km.
            //The cheater cannot win.
        }
        else{
            cout << "The cheater cannot win." << endl;
        }
        people.clear();
    }
    return 0;
}
