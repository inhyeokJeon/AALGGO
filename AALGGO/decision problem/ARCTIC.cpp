//
//  ARCTIC.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/04.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <utility>
#include <cmath>
#include <queue>
#include <cstring>
using namespace std;

ifstream fin("ARCTIC.txt");

int n;

double distances[101][101];

bool decision(double d){
    // 방문했던곳들 표시
    vector<bool> visited(n,false);
    visited[0]= true;
    // 방문했던 곳중 다른 곳으로 연결 가능한 곳을 찾기위해 q를 사용.
    queue<int> q;
    // 처음 0번 방문
    q.push(0);
    int seen =0;
    // 더이상 연결 할 곳이 없을떄 까지
    while(!q.empty()){
        int here = q.front();
        q.pop();
        seen++;
        for(int there=0; there<n; there++){
            // 방문하지 않았고 거리내에 연결 가능 하다면.
            if(!visited[there] && (distances[here][there] <= d)){
                q.push(there);
                visited[there] = true;
            }
                
        }
    }
    // d 거리로 모든 기지를 연결 할 수 있었다면.
    return seen == n;
}
double optimize(){
    double lo = 0, hi = 1415; // root 2000000 = 1414.213---
    for(int i = 0; i<100; i++){
        double mid = (lo + hi)/2.0;
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
        memset(distances,0,sizeof(distances));
        fin >> n;
        vector<pair<double, double> > locations;
        for(int i = 0; i<n; i++){
            double y,x;
            fin >> y >> x;
            locations.push_back(make_pair(y,x));
        }
        for(int i=0; i<n; i++){
            for(int j=i+1; j<n; j++){
                pair<double, double> f = locations[i];
                pair<double, double> s = locations[j];
                // 거리공식 사용
                distances[i][j] = sqrt(pow(f.first-s.first,2) + pow(f.second-s.second,2));
            }
        }
        // 대칭
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                distances[j][i] = distances[i][j];
            }
        }
        printf("%.2f\n",optimize());
    }
}
