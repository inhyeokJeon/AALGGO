//
//  KAKURO2.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/02.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

ifstream fin("KAKURO2.txt");

void initialization();
int n; // 게임판의 크기
const int MAXN = 20;
/*
제약전파 : 한곳을 채우면 다른한곳을 쉽게 채울 수 있다.
채울 순서 정하기 : 적은 수로 구현할 수 있는 것부터.
후보의 수 계산하기 : getCandidate() 힌트에 해당하는 후보숫자들의 목록을 반환하는 함수 구현
후보의 수 빠르게 계산하기 getCandidate()을 좀더 효율적으로 구현하는 generateCandidates()구현
 */

// mask에 속한 원소들의 개수 반환
int getSize(int mask){
    return __builtin_popcount(mask);
}

// mask에 속한 원소들의 합을 반환
int getSum(int mask){
    int sum=0;
    for(int i=0; i<10; i++)
        if (mask & (1 << i)){
            sum += i;
        }
    return sum;
}
/*
int getCandidate(int len, int sum, int known){
    // 조건에 부합하는 집합들의 교집합
    int allSets = 0;
    for(int set=2; set<1024; set = set+2){
        if((set&known) && (getSize(set)==len) && getSum(set)==sum){
            allSets |= set;
        }
    }
    return (allSets&~known);
}
 */
// len / sum / known
int candidates[10][46][1024];

void generateCandidates(){
    memset(candidates, 0, sizeof(candidates));
    for(int set=0; set< 1024; set+=2){
        int length = getSize(set);
        int sum = getSum(set);
        int subset = set;
        while(true){
            candidates[length][sum][subset] |= (set &~subset);
            if(subset == 0) break;
            subset = (subset - 1) & set;
        }
    }
}
// 게임판의 정보
// 카쿠로의 조합 탐색을 위한 유틸리티 함수들
// color : 각 칸의 색깔(0 : 검은칸 혹은 힌트칸, 1 = 흰칸)
// value: 각 흰 칸에 쓴 숫자(아직 쓰지 않은 칸은 0)
// hint : 각 칸에 해당하는 두 힌트의 번호
int color[MAXN][MAXN], value[MAXN][MAXN], hint[MAXN][MAXN][2];
// 각 힌트의 정보
// sum   : 힌트 칸에 쓰인 숫자
// length: 힌트 칸에 해당하는 힌 칸의 수
// known : 힌트 칸에 해당하는 흰 칸에 쓰인 숫자들의 집합
int q, sum[MAXN*MAXN], length[MAXN*MAXN], known[MAXN*MAXN];
//( y,x) 에 val을 쓴다.
void put(int y, int x, int val){
    for(int h=0; h<2; h++){
        known[hint[y][x][h]] += (1<<val);
    }
    value[y][x] = val;
}
// (y,x) 에 쓴 val을 지운다.
void remove(int y, int x, int val){
    for(int h=0; h<2; h++){
        known[hint[y][x][h]] -= (1<<val);
    }
    value[y][x] = 0;
}
// 힌트 번호가 주어질 때 후보의 집합을 반환한다.
int getCandHint(int hint){
    return candidates[length[hint]][sum[hint]][known[hint]];
}
// 좌표가 주어질 때 해당 칸에 들어갈 수 있는 후보의 집합을 반환한다.
int getCandCoord(int y, int x){
    return getCandHint(hint[y][x][0]) & getCandHint(hint[y][x][1]);
}
void printSolution(){
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << value[i][j] << " ";
        }
        cout << endl;
    }
}
// 실제 탐색
// 11. 14 todo
bool search(){
    // 아직 숫자가 쓰지 않은 흰 칸 중에서 후보의 수가 최소인 칸을 찾는다.
    int y= -1, x = -1, minCands = 1023;
    for(int i=0; i <n; i++){
        for(int j=0; j<n; j++){
            if(color[i][j]==1 && value[i][j] == 0){
                int cands = getCandCoord(i,j);
                if(getSize(minCands) > getSize(cands)){
                    minCands = cands;
                    y = i;
                    x = j;
                }
            }
        }
        if(minCands == 0) return false;
    }
    // 모든 칸이 채워졌으면
    if(y ==-1){
        printSolution();
        return true;
    }
    for(int val = 1; val <=9; val++){
        if(minCands &(1<<val)){
            put(y,x,val);
            if(search()) return true;
            remove(y,x,val);
        }
    }
    return false;
}

void read(){
    fin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            fin >> color[i][j];
        }
    }
    int hintNum;
    fin >> hintNum;
    int y,x,direction;
    
    // 0은 가로 힌트, 1은 세로힌트를 의미
    int dy[2] = { 0, 1 };
    int dx[2] = { 1, 0 };
    for(int i=0; i<hintNum; i++){
        fin >> y >> x >> direction >> sum[i];
        y--;
        x--;
        length[i]=0;
        while(true) {
            // 벽을 만날떄 까지 계속 ~
            y += dy[direction]; x += dx[direction];
            if(y >= n || x >= n || color[y][x] == 0) break;
            hint[y][x][direction] = i;
            length[i]++;
        }
    }
    
}
int main(){
    int test_case;
    fin >> test_case;
    generateCandidates();
    
    for(int test =0; test<test_case; test++){
        initialization();
        read();
        search();
    }
}
void initialization(){
    memset(color, 0, sizeof(color));
    memset(value, 0, sizeof(value));
    memset(hint, 0, sizeof(hint));
    memset(sum, 0, sizeof(sum));
    memset(length, 0, sizeof(length));
    memset(known, 0, sizeof(known));
}
