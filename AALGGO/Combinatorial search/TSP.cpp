//
//  TSP.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/26.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <bitset>
using namespace std;
ifstream fin("TSP.txt");

const double INF = 1e200;
const int MAX = 20;
int n; // 도시의 수
double dist[MAX][MAX]; // 두 도시간의 거리를 저장.
vector<int> nearest[MAX]; // 각 도시마다 가까운 순서대로 정렬해 둔다.
double best; // 지금까지 최적해
double minEdge[MAX]; // 각 도시의 가장 짧은 거리를 저장해둔다.
vector<pair<double, pair<int, int> > > edges;
const int CACHED_DEPTH = 5; // 다섯개 남았을떄 DP 사용한다.
map<int, double> cache[MAX][CACHED_DEPTH+1];

struct DisjointSet{
    int num, component;
    vector<int> parent, rank;
    DisjointSet(int n) : num(n), component(n), parent(n), rank(n){
        for(int i=0; i<num; i++){
            parent[i] = i;
            rank[i] = 0;
        }
    }
    int find(int here){
        if(here == parent[here]) // 부모 노드를 찾으면 리턴
            return here;
        return parent[here] = find(parent[here]);
    }
    bool merge(int a, int b){ // a가 포함된 집합과 b가 포함된 집합을 합친다
        a = find(a);
        b = find(b);
        if(a==b)
            return false; // 이미 연결되어 있음
        if(rank[a] > rank[b])
            swap(a,b);
        parent[a] = b;
        if(rank[a] == rank[b]) rank[b]++;
        component--;
        return true;
    }
};

//남은 도시 수가 CACHED_DEPTH 이하개이면 dp로 푼다.
double dp(int here, int visited){
    if(visited == (1<<n) -1) return dist[here][0];
    // 메모이제이션
    int remaining = n - __builtin_popcount(visited); // __builtin_popcount 비트 1의 개수를 리턴해줌.
    double &ret = cache[here][remaining][visited];
    if(ret > 0) return ret;
    ret = INF;
    for(int next = 0; next<n; next++){
        if(visited & (1<<next)) continue; // 방문 했으면;
        ret = min(ret , dp(next, visited + (1<<next)) + dist[here][next]);
    }
    return ret;
}
double mstHeuristic(int here, const vector<bool>& visited){
    DisjointSet DS(n);
    double taken = 0;
    for(int i=0; i<edges.size(); i++){
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if(a!=0 && a!=here && visited[a]) continue;
        if(b!=0 && b!=here && visited[b]) continue;
        if(DS.merge(a,b)) taken += edges[i].first;
    }
    return taken;
}
/* 최소길이만 따짐 mst보다 성능 안좋음
double simpleHeuristic(vector<bool>& visited){
    double ret = minEdge[0];
    for(int i=0; i<n; i++){
        if(!visited[i])
            ret+= minEdge[i];
    }
    return ret;
}
*/

bool pathReversePruning(const vector<int>& path){
    if(path.size()< 3) return false;
    int b = path[path.size()-2];
    int q = path[path.size()-1];
    for(int i=0; i+2 < path.size(); i++){
        int p = path[i];
        int a = path[i+1];
        if(dist[a][p] + dist[b][q] > dist[a][q] + dist[b][p]) return true;
    }
    return false;
}

void search(vector<int>& path, vector<bool>& visited, double currentLength){
    int here = path.back();
    // 뒤집었을때 더 짧다면
    if(pathReversePruning(path)) return;
    //현재 길이 + 남은 도시의 mst최소 길이 합 보다 작다면 최적값이 되지못함.
    if(best <= currentLength + mstHeuristic(here, visited)) return;
    
    // 기저사례 남은 도시 수가 CAHCED_DEPTH 이하면 dp 사용
    if(path.size() + CACHED_DEPTH >= n ) {
        int mask = 0;
        for(int i=0 ; i<n; i++){
            if(visited[i]) mask += (1<<i);
        }
        double cand = currentLength + dp(here, mask);
        best = (best > cand) ? cand : best;
        return ;
    }
    
    for(int i = 0; i < nearest[here].size(); i++){
        int next = nearest[here][i];
        if(visited[next]) continue;
        visited[next] = true;
        path.push_back(next);
        search(path, visited, currentLength + dist[here][next]);
        path.pop_back();
        visited[next] = false;
    }
    
}

double solve(){
    // edges 설정
    edges.clear();
    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++){
            edges.push_back(make_pair(dist[i][j], make_pair(i,j)));
        }
    }
    sort(edges.begin(), edges.end());
    /* mst보다 느림
    // minEdge 제일가까운 간선 저장 하는것 초기화
    for(int i=0; i<n; i++){
        minEdge[i] = INF;
        for(int j=0; j<n; j++){
            if(i!=j) minEdge[i] = min(minEdge[i],dist[i][j]);
        }
    }
    */
    // nearest 각 도시에서 가장 가까운 도시순 대로 정렬
    for(int i=0; i<n; i++){
        vector<pair<double,int> > order;
        for(int j=0 ; j<n; j++){
            if(i!=j) order.push_back(make_pair(dist[i][j], j));
        }
        sort(order.begin(),order.end());
        nearest[i].clear();
        for(int j=0; j<n-1; j++) nearest[i].push_back(order[j].second);
    }
    
    //cache 초기화
    for(int i=0; i<MAX; i++){
        for(int j=0; j<=CACHED_DEPTH; j++)
            cache[i][j].clear();
    }
    best = INF;
    
    for(int i=0; i<n; i++){
        vector<int> path(1,i);
        vector<bool> visited(n, false);
        visited[i] = true;
        search(path, visited,0);
    }
    
    return best;
}

int main(){
    int test_case = 0;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        fin >> n;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                fin >> dist[i][j];
            }
        }
        cout.precision(10);
        cout.setf(ios::fixed, ios::floatfield);
        cout << solve() << endl;
    }
}


/*
TSP1 해결법 완전탐색.
 
double shortestPath(vector<int>& path, vector<bool>& visited, double currentLength) {
  // 기저 사례: 모든 도시를 다 방문했을 때는 0번 도시로 돌아가고 종료한다
  if(path.size() == n)
    return currentLength + dist[0][path.back()];

  double ret = INF; // 매우 큰 값으로 초기화

  // 다음 방문할 도시를 전부 시도해 본다
  for(int next = 0; next < n; ++next) {
    if(visited[next]) continue;
    int here = path.back();

    path.push_back(next);
    visited[next] = true;

    // 나머지 경로를 재귀호출을 통해 완성하고 가장 짧은 경로의 길이를 얻는다
    double cand = shortestPath(path, visited, currentLength + dist[here][next]);
    ret = min(ret, cand);

    visited[next] = false;
    path.pop_back();
  }

  return ret;
}
*/


/*
 dp를 이용해 TSP2 풀기.
 
//double cache[MAX][1<<MAX];

// here: 현재 위치
// visited: 각 도시의 방문 여부
// here 에서 시작해 남은 도시들을 방문할 수 있는 최단 경로의 길이를 반환한다.
// 나머지 도시들을 모두 방문하는 경로들 중 가장 짧은 것의 길이를 반환한다
double shortestPath2(int here, int visited) {
// 기저 사례: 모든 도시를 다 방문했을 때는 0번 도시로 돌아가고 종료한다
if(visited == (1<<n)-1) return dist[here][0];

// 메모이제이션
double& ret = cache[here][visited];
if(ret >= 0) return ret;

ret = INF; // 매우 큰 값으로 초기화

// 다음 방문할 도시를 전부 시도해 본다
for(int next = 0; next < n; ++next) {
// 이미 방문한 도시인 경우
if(visited & (1<<next)) continue;

double cand = dist[here][next] + shortestPath2(next, visited + (1<<next));
ret = min(ret, cand);
}

return ret;
}
*/
