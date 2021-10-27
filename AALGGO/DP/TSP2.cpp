//
//  TSP2.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/27.
//

#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream fin("TSP.txt");

const int MAX = 15;
const double INF = 1e200;
double cache[MAX][1<<MAX];
int N;
double dist[MAX][MAX];
// here: 현재 위치
// visited: 각 도시의 방문 여부
// here 에서 시작해 남은 도시들을 방문할 수 있는 최단 경로의 길이를 반환한다.
// 나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환한다
double shortestPath2(int here, int visited) {
// 기저 사례: 모든 도시를 다 방문했을 때는 0번 도시로 돌아가고 종료한다
    if(visited == (1<<N)-1) return 0;
    // 메모이제이션
    double& ret = cache[here][visited];
    if(ret > 0) return ret;

    ret = INF; // 매우 큰 값으로 초기화

    // 다음 방문할 도시를 전부 시도해 본다
    for(int next = 0; next < N; ++next) {
        // 이미 방문한 도시인 경우
        if(visited & (1<<next)) continue;
        double cand = dist[here][next] + shortestPath2(next, visited + (1<<next));
        ret = min(ret, cand);
    }
    return ret;
}

void initialize(){
    for(int i=0 ; i<MAX; i++){
        for(int j=0; j<(1<<MAX); j++){
            cache[i][j] = -1.0;
        }
    }
}
int main(){
     
     int test_case = 0;
     fin >> test_case;
     for(int test=0; test<test_case; test++){
         fin >> N;
         for(int i=0; i<N; i++){
             for(int j=0; j<N; j++){
                 fin >> dist[i][j];
             }
         }
         initialize();
         
         cout.setf(ios::fixed, ios::floatfield);
         double result= INF;
         for(int i=0; i<N; i++){
             result = min(result, shortestPath2(i,(1<<i)));
         }
         cout.precision(10);
         cout << result << endl;
     }
     return 0;
 }
