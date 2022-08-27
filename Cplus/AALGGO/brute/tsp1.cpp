//
//  tsp1.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/26.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
 
const int MAX = 8; //3<=n<=8

ifstream fin("tsp.txt");

int n; //도시의 수
double dist[MAX][MAX]; //두 도시간의 거리를 저장하는 배열
//path:지금까지 만든 경로
//visited: 각 도시의 방문 여부
//currentLength: 지금까지 만든 경로의 길이
//나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환
double shortestPath(int n, vector<int> &path, vector<bool> &visited, double currentLength)
{
    //기저 사례:모든 도시를 다 방문했을 때는 시작 도시로 돌아가고 종료한다
    if (path.size() == n)
       return currentLength;
    double result = numeric_limits<double>::max(); //매우 큰 값으로 초기화
    //다음 방문할 도시를 전부 시도
    for (int next = 0; next < n; next++)
    {
       if (visited[next])
           continue;
       int here = path.back();
       path.push_back(next);
       visited[next] = true;
       //나머지 경로를 재귀 호출을 통해 완성하고 가장 짧은 경로의 길이를 얻는다
       double candidate = shortestPath(n, path, visited, currentLength + dist[here][next]);
       result = min(result, candidate);
       visited[next] = false;
       path.pop_back();
    }
    return result;
}
 
int main(void)
{
    int test_case;
    double result;
    fin >> test_case;
    for (int i = 0; i < test_case; i++)
    {
       fin >> n;
       //거리 입력
       for (int j = 0; j < n; j++)
           for (int k = 0; k < n; k++)
           {
              fin >> dist[j][k];
           }
      
       double answer = numeric_limits<double>::max(); //중요

       for (int j = 0; j < n; j++)
       {
           vector<int> path(1, j); //j번째 도시에서 출발
           vector<bool> visited(n, false);
           visited[j] = true; //출발했으므로 방문
           result = shortestPath(n, path, visited, 0.0000000000);
           if (answer > result) //기존보다 크면 덮어쓰지 않는다
              answer = result;
       }
       printf("%.10f\n", answer);
    }
    return 0;
}

