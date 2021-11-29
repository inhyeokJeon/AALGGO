//
//  ROOTS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/07.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("ROOTS.txt");

int N; // 방정식의 차수
// 미분한 결과 p의 계수를 리턴
vector<double> differentiate(const vector<double>& poly){
    int degree = poly.size() -1;
    vector<double> result;
    for(int i=0; i< degree; i++){
        result.push_back(poly[i]*(degree-i) );
    }
    return result;
}
// 2차 이하 방정식이 주어지면 해를 리턴함
vector<double> solveNaive(const vector<double> &poly){
    int degree = poly.size() -1;
    vector<double> result;
    if(degree == 2){
        double a= poly[0], b = poly[1], c = poly[2];
        if((pow(b,2) - 4*a*c) <0 ){ // 근이 존재하지 않을 경우
            result.push_back(987654321);
            return result;
        }
        // 근의 공식
        double first = (-b+sqrt(pow(b,2) - 4*a*c)) / (2*a) ;
        double second = (-b-sqrt(pow(b,2) - 4*a*c)) / (2*a) ;
        if(first > second){ swap(first,second);}
        result.push_back(first);
        result.push_back(second);
    }
    else if(degree == 1){
        result.push_back(-(poly[1]/poly[0]));
    }
    return result;
}
// f(x0) 가 주어지면 답을 리턴함.
double evaluate(const vector<double> &poly, double x0){
    int degree = poly.size();
    double sum = 0;
    for(int i=0; i<degree; i++){
        sum += poly[i]*pow(x0,(degree-1-i));
    }
    return sum;
}
const double L = 10;

vector<double> solve(const vector<double> &poly){
    int degree = poly.size() - 1;
    if(degree <= 2){
        return solveNaive(poly);
    }
    vector<double> temp = differentiate(poly);
    vector<double> range = solve(temp);
    // 맨앞과 맨뒤에 L크기를 추가한다.
    range.insert(range.begin(), -L-1);
    range.insert(range.end(), L + 1);
    vector<double> result;
    for(int i=0; i< range.size()-1; i++){
        double x1 = range[i], x2 = range[i+1];
        double y1 = evaluate(poly, x1), y2 = evaluate(poly, x2);
        if(y1*y2 > 0) continue; // 같은부호이면 해를 가지지 않기 때문.
        // 증가하는 방향으로 생각한다.
        if(y1 > y2) { swap(x1,x2); swap(y1,y2);}
        // 100 번을 쪼개 최적값을 찾는다.
        for(int it = 0; it<100; it++){
            double mid_x = (x1+x2)/2.0;
            double mid_y = evaluate(poly, mid_x);
            if(mid_y*y1 > 0){
                x1 = mid_x;
                y1 = mid_y;
            }
            else{
                x2 = mid_x;
                y2 = mid_y;
            }
        }
        result.push_back((x1+x2)/2.0);
    }
    sort(result.begin(),result.end());
    return result;
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        fin >> N ;
        vector<double> poly;
        for(int i=0; i< N+1; i++){
            double degree;
            fin >> degree;
            poly.push_back(degree);
        }
        vector<double> result = solve(poly);
        for(int i=0; i<result.size(); i++){
            printf("%0.8f ",result[i]);
        }
        cout << endl;
        
    }
    
}
