//
//  GRADUATION.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/26.
//


#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
ifstream fin("GRADUATION.txt");

int N; // 전공 과목수
int K; // 들어야할 과목수
int L; // 태우가 한학기에 들을 수 있는 최대 과목 수
int M; // 학기 수
const int MAXN = 12;
int pre_classes[MAXN];// 선수과목
int semester_classes[10]; // 해당 학기에 들을 수 있는 과목들
int cache[10][1<<MAXN];
const int INF = 987654321;
int bitcount(int taken){
    return __builtin_popcount(taken);
}
// semester - 학기
// taken - 지금까지 수강한 강의
int graduate(int semester, int taken){
    // 기저 사례 과목수를 다채웟으면 학기 리턴;
    if(bitcount(taken) >= K) return 0;
    // 과목수를 다 못채우면 INF 리턴
    if(semester == M) return INF;
    // 학기수 과목수
    int &ret = cache[semester][taken];
    if(ret!=-1 ) return ret;
    ret = INF;
    // 이번학기에 들을 수 있고 이미 듣지 않은것들
    int canTake = ( semester_classes[semester] & ~taken);
    for(int i = 0; i<N; i++){
        if((canTake & (1<< i)) && (pre_classes[i]&taken)!=pre_classes[i] ){
            canTake &= ~(1<<i);
        }
    }
    // 수강할 수 있는 과목들의 경우의 수를 모두 순회한다.
    for(int take = canTake ; take>0; take=((take-1)&canTake)){
        if(bitcount(take)>L) continue;
        ret= min(ret, graduate(semester+1, take|taken)+1);
    }
    // 휴학한 것으로 취급
    // 학기 수에 포함하지않는다.
    ret = min(ret, graduate(semester +1, taken));
    return ret;
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test<test_case; test++){
        fin >> N >> K >> M >> L;
        memset(pre_classes, 0, sizeof(pre_classes));
        memset(semester_classes, 0, sizeof(semester_classes));
        memset(cache, -1 , sizeof(cache));
        for(int i=0; i<N; i++){
            int R; fin >> R;
            for(int j=0; j<R; j++){
                int ri; fin >> ri;
                pre_classes[i] |= (1 << ri);
            }
        }
        for(int i=0; i<M; i++){
            int C; fin >> C;
            for(int j=0; j<C; j++){
                int ci; fin >> ci;
                semester_classes[i] |= (1<< ci);
            }
        }
        int result = graduate(0,0);
        if(result == INF){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            cout<< result << endl;
        }
    }
}
