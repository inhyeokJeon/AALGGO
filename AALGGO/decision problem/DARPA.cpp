//
//  DARPA.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/03.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream fin("DARPA.txt");

int n; // 카메라의 개수
int m; // 설치 가능한 중계소의 수
int min_distance;
bool solution(const vector<double> &locations, int cameras, double gap){
    double limit = -1;
    int installed = 0;
    for(int i=0; i<locations.size(); i++){
        if(limit <= locations[i]){
            installed++;
            limit = locations[i] + gap;
        }
    }
    return installed >=cameras;
}
double optimize(const vector<double> &locations, int cameras){
    double lo=0, hi = 241;
    for(int i=0; i<100; i++){
        double mid = (lo+hi)/2.0;
        if(solution(locations,cameras,mid)){
            lo = mid;
        }
        else{
            hi = mid;
        }
    }
    return lo;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        fin >> n >> m;
        vector<double> locations;
        for(int i = 0; i<m; i++){
            double location;
            fin >> location;
            locations.push_back(location);
        }
        printf("%0.2f\n",optimize(locations,n));

    }
}
