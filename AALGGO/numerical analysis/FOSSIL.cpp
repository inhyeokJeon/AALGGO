//
//  FOSSIL.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/11.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;
ifstream fin("FOSSIL.txt");
struct point{
    double x,y;
};

int n; // 첫번째 다각형의 좌표 수
int m; // 두번째 다각형의 좌표 수
vector<point> hull1, hull2; // 다각형의 좌표
vector<pair<point, point> > upper, lower; // 윗껍질과 아래껍질 다각형
void Clear(); 
double minX(const vector<point> &hull){
    double result = hull[0].x;
    for(int i = 1; i<hull.size(); i++){
        result = min(result, hull[i].x);
    }
    return result;
}
double maxX(const vector<point> &hull){
    double result = hull[0].x;
    for(int i = 1; i<hull.size(); i++){
        result = max(result, hull[i].x);
    }
    return result;
}

// 윗 껍질과 아래껍질로 나누고 저장
void decompose(const vector<point> &hull){
    int n = hull.size();
    for(int i=0; i<n; i++){
        // hull이 반시계 방향이므로
        // x 가 증가할 때 -> 아래 껍질에 속하는것
        if(hull[i].x < hull[(i+1)%n].x){ // 모듈러 n을 해주는 이유는 맨 끝 좌표에서 원점으로 가는 경우때문
            lower.push_back(make_pair(hull[i], hull[(i+1)%n]));
        }
        // x 가 감소 -> 위 껍질에 속함
        else if(hull[i].x > hull[(i+1)%n].x){
            upper.push_back(make_pair(hull[i],hull[(i+1)%n]));
        }
    }
}

// [a.x, b.x] 구간안에 있는지를 판별한다.
bool between(const point &a,const point &b, const double x){
    return (a.x <= x <= b.x) || (b.x <= x <= a.x);
}

// 선분이 과 x값이 교차하는 점의 y값을 반환한다
double at(const point &a, const point &b, double x){
    double inclination = (b.y-a.y)/(b.x-a.x);
    double y_intercept = a.y-(inclination*a.x);
    return inclination*x + y_intercept;
}

// x 좌표가 주어질 때 잘린 부분의 길이를 반환
double vertical(double x){
    // minUp -> 윗껍질 사이의 최소 길이
    // maxLow -> 아래껍질 사이의 최대 길이
    // (겹치는 부분의 최대 길이를 구해야 하기 때문에)
    double minUp = 101, maxLow= -1;
    for(int i=0; i<upper.size(); i++){
        if(between(upper[i].first,upper[i].second,x)){
            minUp = min(minUp, at(upper[i].first, upper[i].second,x));
        }
    }
    for(int i=0; i<lower.size(); i++){
        if(between(lower[i].first, lower[i].second, x)){
            maxLow = max(maxLow, at(lower[i].first,lower[i].second,x));
        }
    }
    return minUp-maxLow;
    
}

double solve(){
    double lo = max(minX(hull1),minX(hull2));
    double hi = min(maxX(hull1),maxX(hull2));
    if(hi<lo) return 0;
    for(int it = 0; it<100; it++){
        double oneThird = (2*lo + hi)/3;
        double twoThird = (lo + 2*hi)/3;
        if(vertical(oneThird) < vertical(twoThird)){
            lo = oneThird;
        }
        else {
            hi = twoThird;
        }
    }
    // 안겹치면 0
    return max(0.0,vertical(hi));
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        fin >> n >> m;
        point temp;
        for(int i=0; i< n; i++){
            fin >> temp.x >> temp.y;
            hull1.push_back(temp);
        }
        for(int i=0; i<m; i++){
            fin >> temp.x >> temp.y;
            hull2.push_back(temp);
        }
        decompose(hull1);
        decompose(hull2);
        printf("%0.10f\n",solve());
        Clear();
        //cout << solve() << endl;
    }
}

void Clear(){
    hull1.clear();
    hull2.clear();
    lower.clear();
    upper.clear();
}
