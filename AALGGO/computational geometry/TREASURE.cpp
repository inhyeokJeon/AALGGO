//
//  TREASURE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/15.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cassert>
using namespace std;

ifstream fin("TREASURE.txt");
const double EPSILON = 1e-9;
const double INFTY = 1e200;
const double PI = 2.0*acos(0.0);

struct vector2{
    double x,y;
    // 생성자를 explicit로 지정하면 실수가 들어가는 일을 방지해준다.
    explicit vector2(double _x = 0, double _y = 0) : x(_x), y(_y)
    {}
    // 두 벡터의 비교
    bool operator == (const vector2 &rhs) const {
        return x== rhs.x && y==rhs.y;
    }
    // 대소 비교 x가 같지않으면 x 값으로 비교 아니면 y 값으로 비교
    bool operator < (const vector2 &rhs) const {
        return (x!=rhs.x) ? x<rhs.x : y<rhs.y;
    }
    // 벡터끼리의 덧셉, 뺄셈
    vector2 operator + (const vector2 & rhs) const{
        return vector2(x+rhs.x,y+rhs.y);
    }
    vector2 operator - (const vector2 & rhs) const{
        return vector2(x-rhs.x,y-rhs.y);
    }
    // 벡터에 실수를 곱함
    vector2 operator * (double rhs) const{
        return vector2(x*rhs, y*rhs);
    }
    // 벡터의 길이를 반환 hypot -> sqrt(x^2+y^2)
    double norm() const{ return hypot(x,y); }
    // 방향이 같은 단위 벡터(unit vector)를 반환한다.
    vector2 normalize() const{
        return vector2(x/norm(), y/norm());
    }
    // x축의 양의 방향으로부터 이 벡터까지 반시계 방향으로 잰 각도
    double polar() const { return fmod(atan2(y,x) +2*PI, 2*PI);}
    // 벡터의 내적
    double dot(const vector2 &rhs) const{
        return x*rhs.x + y*rhs.y;
    }
    // 벡터의 외적 , 두 벡터가 이루는 사각형의 넓이
    double cross(const vector2 &rhs) const{
        return x*rhs.y - y*rhs.x;
    }
    // 이 벡터를 rhs에 사영한 결과
    vector2 project(const vector2 &rhs) const{
        vector2 r = rhs.normalize();
        return r*r.dot(*this);
    }
    void print(){
        cout << "x : " << x << " y  : " << y << endl;
    }
};

double howMuchCloser(vector2 p, vector2 a, vector2 b){
    return (b-p).norm() - (a-p).norm();
}
// 원점에서 벡터 b가 벡터 a의 반시계 방향이면 양수, 시계 방향이면 음수,
// 평행이면 0을 반환한다.
double ccw(vector2 a, vector2 b){
    return a.cross(b);
}
// 점 p를 기준으로 벡터 b가 벡터 a의 반시계 방향이면 양수, 시계 방향이면 음수,
// 평행이면 0을 반환한다.
double ccw(vector2 p, vector2 a, vector2 b){
    return ccw(a-p, b-p);
}

// (a,b)를 포함하는 선과 (c,d)를 포함하는 선의 교점을 x에 반환한다.
// 두 선이 평행이면 (겹치는 경우를 포함) 거짓, 아니면 참을 반환.
bool lineIntersection(vector2 a,vector2 b, vector2 c, vector2 d, vector2 &x){
    double det = (b-a).cross(d-c);
    if(fabs(det) < EPSILON) return false;
    x = a+ (b-a)*((c-a).cross(d-c) / det);
    return true;
}
// (a,b)와 (c,d)가 평행한 두 선분일 때 이들이 한 점에서 겹치는지를 확인한다.
bool parallelSegments(vector2 a, vector2 b, vector2 c, vector2 d, vector2 &p){
    if(b<a) swap(a,b);
    if(d<c) swap(c,d);
    // 한 직선 위에 없거나 두 선분이 겹치지 않는 경우를 걸러낸다.
    if(ccw(a,b,c) !=0 || b<c || d<a) return false;
    // 두 선분은 확실히 겹친다. 교차점을 찾자
    if(a<c) p=c; else p=a;
    return true;
}
// p 가(a,b)를 감싸면서 각 변이 x,y축에 평행한 최소 사각형 내부에 있는지 확인한다.
// a,b,p는 일직선 상에 있다고 가정한다.
bool inBoundingRectangle(vector2 p, vector2 a, vector2 b){
    if(b<a) swap(a,b);
    return p==a || p==b  || (a<p && p<b);
}
//(a,b) 선분과 (c,d) 선분의 교점을 p에 반환한다.
// 교점이 여러 개일 경우 아무 점이나 반환한다.
// 두 선분이 교차하지 않을 경우 false 를 반환한다.
bool segmentIntersection(vector2 a, vector2 b, vector2 c, vector2 d, vector2 &p){
    // 두 직선이 평행인 경우 예외처리
    if(!lineIntersection(a, b, c, d, p))
        return parallelSegments(a, b, c, d, p);
    // p가 두 선분에 포함되어 있는 경우에만 참을 반환
    return inBoundingRectangle(p, a, b) && inBoundingRectangle(p, c, d);
}
// 두 선분이 서로 접촉하는지 여부를 판단한다.
bool segmentIntersects(vector2 a, vector2 b, vector2 c, vector2 d){
    double ab= ccw(a,b,c) * ccw(a,b,d);
    double cd = ccw(c,d,a) * ccw(c,d,b);
    // 두 선분이 한직선 위에 있거나 끝점이 겹치는 경우
    if(ab == 0 && cd == 0){
        if(b<a) swap(a,b);
        if(d<c) swap(c,d);
        return !(b<c ||d<a);
    }
    return ab<=0 && cd <=0;
}
// 점 p 에서 (a,b) 직선에 내린 수선의 발을 구한다.
vector2 perpendicularFoot(vector2 p, vector2 a, vector2 b){
    return a+(p-a).project(b-a);
}

// 점 p와 (a,b) 직선 사이의 거리를 구한다.
double pointToLine(vector2 p,vector2 a, vector2 b){
    return (p-perpendicularFoot(p, a, b)).norm();
}


// 단순 다각형 P의 넓이를 구한다.
// p 는 각 꼭지점의 위치 벡터의 집합으로 주어진다.
double area(const vector<vector2>& p){
    double ret =0;
    for(int i=0; i<p.size(); i++){
        int j=(i+1)%p.size();
        ret += p[i].x*p[j].y - p[j].x * p[i].y;
    }
    return fabs(ret) / 2.0;
}
// 점 q 가 다각형 p안에 포함되어 있을 경우 참 아니면 거짓을 반환.
// q의 다각형의 겨계 위에 있는 경우의 반환값은 정의되어 있지않음.
bool isInside(vector2 q, const vector<vector2> &p){
    int crosses = 0;
    for(int i=0; i<p.size(); i++){
        int j= (i+1) % p.size();
        // (p[i], p[j] 가 반직선을 세로로 가로지르는가?
        if((p[i].y > q.y) != (p[j].y)> q.y){
            // 가로지르는 x 좌표를 계산한다.
            double atX = (p[j].x - p[i].x)*(q.y - p[i].y) / (p[j].y - p[i].y) + p[i].x;
            if(q.x < atX ){
                crosses++;
            }
        }
    }
    // 홀수번 교차하면 내부에 있는것 짝수면 외부
    return crosses %2 > 0;
}
// ------- 문제

typedef vector<vector2> polygon;

polygon cutPoly(const polygon &p, const vector2 &a, const vector2 &b){
    int n = p.size();
    vector<bool> inside(n);
    // 각 점이 반평면 안에 있는지 확인한다.
    for(int i=0; i< n; i++){
        inside[i] = ccw(a,b,p[i]) >= 0;
    }
    polygon ret;
    // 다각형의 각 변을 순회 하면서 결과 다각형의 각 점을 반환한다.
    for(int i=0; i<n ;i++){
        int j = (i+1) %n;
        // 반평면 내에 있는 점 p[i] 는 항상 결과 다각형에 포함된다.
        if(inside[i]) ret.push_back(p[i]);
        // 변 p[i]-p[j] 가 직선에 교차하면 교차점을 결과 다각형에 포함시킨다.
        if(inside[i] != inside[j]){
            vector2 cross;
            assert(lineIntersection(p[i], p[j], a, b, cross));
            ret.push_back(cross);
        }
    }
    return ret;
}

polygon intersection(const polygon &p, double x1, double y1, double x2, double y2){
    vector2 a(x1,y1), b(x2, y1), c(x2, y2), d(x1, y2);
    polygon ret = cutPoly(p,a,b);
    ret = cutPoly(ret , b, c);
    ret = cutPoly(ret, c,d);
    ret = cutPoly(ret, d,a);
    return ret;
}
 
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        int x1,y1,x2,y2,N;
        fin >> x1 >> y1 >> x2 >> y2 >> N;
        polygon poly(N);
        for(int i=0; i<N; i++){
            fin >> poly[i].x >> poly[i].y;
        }
        polygon result = intersection(poly,x1,y1,x2,y2);
        printf("%0.10f\n",area(result));
    }
}
