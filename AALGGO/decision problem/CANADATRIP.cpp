//
//  CANADATRIP.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/05.
//


#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <cmath>
#include <tuple>
#include <cstring>
using namespace std;

ifstream fin("CANADATRIP.txt");

int n; // 도시의 수
int k; // k번째 표지판
// tuple(first,second,third)
// first 도시의 거리,
// second 도착 언제전부터 표지판이 표시되는지,
// third 표지판의 간격
vector<tuple<int, int, int>> city;

bool decision(int dist){
    int ret=0;
    for(int i=0; i<n; i++){
        // 거리가 표지판 하나라도 포함하게 된다면
        if(dist >= get<0>(city[i]) - get<1>(city[i])){
            ret += (min(dist,get<0>(city[i])) -  (get<0>(city[i]) - get<1>(city[i]))) / get<2>(city[i])+1;
        }
    }
    return ret >= k;
}

int optimize(){
    int lo=-1, hi = 8030001;
    while(lo+1<hi){
        int mid = (lo+hi)/2;
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
            int l,m,g;
            fin >> l >> m >> g;
            city.push_back(make_tuple(l,m,g));
        }
        cout << optimize() << endl;
        city.clear();
    }
}

