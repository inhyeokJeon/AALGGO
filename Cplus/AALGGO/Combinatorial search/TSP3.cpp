//
//  TSP3.cpp
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
const int CACHED_DEPTH = 5; // 다섯개 남았을떄 DP 사용한다.

int N; // 도시의 수
double best; // 지금까지 최적해

double dist[MAX][MAX]; // 두 도시간의 거리를 저장.
double minEdge[MAX]; // 각 도시의 가장 짧은 거리를 저장해둔다.

vector<int> nearest[MAX]; // 각 도시마다 가까운 순서대로 정렬해 둔다.
vector<pair<double, pair<int, int> > > edges; // 모든 도시간의 도로를 길이 순으로 정렬

map<int, double> cache[MAX][CACHED_DEPTH+1];

struct DisjointSet{
    int num, component;
    vector<int> parent, rank;
    DisjointSet(int N) : num(N), component(N), parent(N), rank(N){
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

/* 최소길이만 따짐 mst보다 성능 안좋음
double simpleHeuristic(vector<bool>& visited){
    double ret = minEdge[0];
    for(int i=0; i<N; i++){
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
        if(dist[p][a] + dist[b][q] > dist[p][b] + dist[a][q]) return true;
    }
    return false;
}

double mstHeuristic(int here, const vector<bool>& visited){
    DisjointSet DS(N);
    double taken = 0;
    for(int i=0; i<edges.size(); i++){
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        if(a!=here && visited[a]) continue;  // 간선이 here가 아니고 방문했던 곳이면 패쓰
        if(b!=here && visited[b]) continue;
        if(DS.merge(a,b)) taken += edges[i].first; // 겹치는 부분이 없으면 상호배타되어 최소의 간선의 합을 구함
    }
    return taken;
}

//남은 도시 수가 CACHED_DEPTH 이하개이면 dp로 푼다.
double dp(int here, int visited){
    
    if(visited == (1<<N) -1) return 0.0;
    // 메모이제이션
    int remaining = N - __builtin_popcount(visited); // __builtin_popcount 비트 1의 개수를 리턴해줌.
    double &ret = cache[here][remaining][visited];
    if(ret > 0) return ret;
    ret = INF;
    for(int next = 0; next<N; next++){
        if(visited & (1<<next)) continue; // 방문 했으면;
        ret = min(ret , dp(next, visited + (1<<next)) + dist[here][next]);
    }
    return ret;
}

void search(vector<int>& path, vector<bool>& visited, double currentLength){
    int here = path.back();
    // 뒤집었을때 더 짧다면
    if(pathReversePruning(path)) return;
    //현재 길이 + 남은 도시의 mst최소 길이 합 보다 작다면 최적값이 되지못함.
    if(best <= currentLength + mstHeuristic(here, visited)) return;
    
    // 기저사례 남은 도시 수가 CAHCED_DEPTH 이하면 dp 사용
    if(path.size() + CACHED_DEPTH >= N ) {
        int mask = 0;
        for(int i=0 ; i<N; i++){
            if(visited[i]) mask += (1<<i);
        }
        double cand = currentLength + dp(here, mask);
        best = (best > cand) ? cand : best;
        return;
    }
    
    for(int i = 0; i < nearest[here].size(); i++){
        int next = nearest[here][i];
        if(visited[next]) continue;
        path.push_back(next);
        visited[next] = true;
        search(path, visited, currentLength + dist[here][next]);
        visited[next] = false;
        path.pop_back();
    }
    
}

double solve(){
    // nearest 각 도시에서 가장 가까운 도시순 대로 정렬
    for(int i=0; i<N; i++){
        vector<pair<double,int> > order;
        for(int j=0 ; j<N; j++){
            if(i!=j) order.push_back(make_pair(dist[i][j], j));
        }
        sort(order.begin(),order.end());
        nearest[i].clear();
        for(int j=0; j<N-1; j++) nearest[i].push_back(order[j].second);
    }
    // edges 설정
    edges.clear();
    for(int i=0; i<N; i++){
        for(int j=0; j<i; j++){
            edges.push_back(make_pair(dist[i][j], make_pair(i,j)));
        }
    }
    sort(edges.begin(), edges.end());
    
    //cache 초기화
    for(int i=0; i<MAX; i++){
        for(int j=0; j<=CACHED_DEPTH; j++)
            cache[i][j].clear();
    }
    best = INF;
    
    for(int i=0; i<N; i++){
        vector<int> path(1,i);
        vector<bool> visited(N, false);
        visited[i] = true;
        search(path, visited,0);
    }
    
    return best;
    
    
    /* mst보다 느림
    // minEdge 제일가까운 간선 저장 하는것 초기화
    for(int i=0; i<N; i++){
        minEdge[i] = INF;
        for(int j=0; j<N; j++){
            if(i!=j) minEdge[i] = min(minEdge[i],dist[i][j]);
        }
    } */
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
        cout.precision(10);
        cout.setf(ios::fixed, ios::floatfield);
        cout << solve() << endl;
    }
    return 0;
}
