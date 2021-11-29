//
//  PINBALL.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/15.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

ifstream fin("PINBALL.txt");
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

//--------------------문제
int N;
vector<vector2> center; //중심
vector<int> radius; //반지름
//2차 방정식의 해를 순서대로 반환한다.
vector<double> solve2(double a, double b, double c){
    double d= b*b - 4*a*c;
    // 해가 없을 경우
    if(d < -EPSILON) return vector<double>();
    // 중근
    if(d < EPSILON) return vector<double>(1,-b/(2*a));
    vector<double> ret;
    ret.push_back((-b -sqrt(d))/(2*a));
    ret.push_back((-b +sqrt(d))/(2*a));
    return ret;
}
// here 에 있던 공이 1초마다 dir만큼 굴러갈 때, center를 중심으로 하고
// 반지름 radius인 장애물과 몇 초 후에 충돌하는지 반환한다.
// 충돌하지 않을경우 아주큰값 INFTY를 반환한다.
double hitCircle(vector2 here, vector2 dir, vector2 center, int radius){
    // 공의 현재 벡터 p, 방향 벡터 q, 시간 t 가 주어질 때
    // 공의 궤적 f(t) = p + t*d
    // 중심이 c이고 반지름이 r인 장애물과 교차하는 시간을 t에 대하여 풀면
    // |c-f(t)| = r -> 양변 제곱 => (c-f(t))*(c-f(t)) = r^2
    // 정리하면 d*d*t^2 + 2(p-c)*d*t + c*c + p*p-2(c*p)-r^2=0
    double a = dir.dot(dir); // d*d
    double b = 2 * dir.dot(here-center); //2(p-c)*d
    double c = center.dot(center) + here.dot(here) - 2*here.dot(center) - radius*radius; // c*c + p*p-2(c*p)-r^2
    vector<double> sols = solve2(a,b,c);
    if(sols.empty() || sols[0] < EPSILON) return INFTY;
    // 두 근중 더 작은 답을 리턴한다.
    return sols[0];
    
}
// here에 있던 공이 dir 방향으로 굴러와 center를 중심으로 하는 장애물에서
// contact 위치에서 충돌 했을 때 공의 새로운 방향을 반환한다.
vector2 reflect(vector2 dir, vector2 center, vector2 contact){
    return (dir - dir.project(contact-center)*2).normalize();
}
void simulate(vector2 here, vector2 dir){
    dir = dir.normalize(); // 방향은 항상 단위 벡터로 저장.
    int hitCount = 0;
    while(hitCount < 100){
        //충돌할 장애물을 찾는다.
        int circle = -1;
        double time = INFTY*0.5;
        // 각 장애물을 순회해 가장 먼저 만나는 장애물을 찾는다.
        for(int i=0; i<N;i++){
            double cand = hitCircle(here, dir, center[i], radius[i] + 1);
            if(cand < time){
                time = cand;
                circle = i;
                
            }
        }
        // 더이상 장애물에 충돌하지 않고 게임판을 벗어난 경우
        if(circle == -1) break;
        if(hitCount++) cout << " ";
        cout << circle;
        // 공의 새 위치를 계산한다.
        vector2 contact = here + dir*time;
        // 부딪힌 위치와 새 방향으로 here와 dir를 변경한다.
        dir = reflect(dir, center[circle], contact);
        here = contact;
    }
    cout << endl;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        center.clear();
        radius.clear();
        int x,y,dx,dy;
        fin >> x >> y >> dx >> dy >> N;
        vector2 here(x,y);
        vector2 dir(dx,dy);
        for(int i=0; i<N; i++){
            int xi,yi,ri;
            fin >> xi >> yi >> ri;
            center.push_back(vector2(xi,yi));
            radius.push_back(ri);
        }
        simulate(here,dir);
    }
}
