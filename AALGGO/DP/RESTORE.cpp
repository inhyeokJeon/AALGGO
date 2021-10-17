//
//  RESTORE.cpp
//  AALGGO
//
//  Created by inhyeoK on 2021/10/11.
//
// 어떤 문자열 조각에도 포함되지 않는 문자를 더할 일은 절대 없다.
// 연속해서 출현하는 문자열들의 접미사와 접두사를 최대한 많이 겹치게 해야
// 가장 짧은 문자열을 찾을 수 있다.
// 한 문자열 조각이 다른 문자열에 포함될 경우 무시하면 된다.
// 전처리 과정에서 조각들을 입력받자마자 문자열 중 다른 문자열에 포함된 것이 있나 살피고 이들을 다 지워 버리도록 한다.
//

#include <iostream>
#include <cstring> // memset
#include <fstream>
#include <string> // string
#include <algorithm> // sort

using namespace std;

ifstream fin("RESTORE.txt");

const int MAX_N = 15;
int K;
string word[MAX_N];
int cache[MAX_N][1<<MAX_N] , overlap[MAX_N][MAX_N];

void preCalc(){
    for(int i=0; i<K; i++){
        for(int j=0; j<K; j++){
            for(int length = min(word[i].size(), word[j].size()); length>0; length-- ){
                if(word[i].substr(word[i].size()-length) == word[j].substr(0,length)){
                    overlap[i][j] = length;
                    break;
                }
            }
        }
    }
    return;
}

// last : 마지막에 출현한 조각
// used : 지금까지 출현한 조각 집합.
int restore(int last, int used){
    //기저 사례
    if(used == (1<<K)-1) return 0;
    //memoization
    int &ret = cache[last][used];
    if(ret!=-1) return ret;
    ret = 0;
    for(int next = 0; next < K ; next++)
        if((used & (1<<next)) == 0) {
            int cand = overlap[last][next] + restore(next, used + (1<<next));
            ret = max(ret,cand);
        }
    return ret;
}

string reconstruct(int last, int used){
    if(used==(1<<K)-1) return "";
    for(int next = 0; next < K ; next++){
        // next 가 이미 사용되었으면 패쓰
        if(used & (1<<next)) continue;
        // next를 사용했을 경우의 답이 최적해와 같다면 next 사용
        int ifUsed = overlap[last][next] + restore(next, used + (1<<next));
        if(restore(last,used) == ifUsed)
            return (word[next].substr(overlap[last][next]) + reconstruct(next, used + (1<<next)));
    }
    return "ERRORRORO";
}
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    for(int i = 0; i < test_case; i++){
        fin >> K;
        memset(cache, -1, sizeof(cache));
        memset(overlap, 0, sizeof(overlap));
        for(int j=0; j<K; j++){
            fin >> word[j];
        }
        
        while (true)
       {
           bool removed = false;
           for(int j=0; j<K && !removed; j++)
              for(int k=0; k<K; k++)
                  if (j != k && word[j].find(word[k]) != -1) //부분문자열이 겹친다면 삭제
                  {
                      //heapSort 삭제와 비슷한 과정
                      word[k] = word[K - 1]; //맨 끝에 있는 string과 위치변경
                      K--;
                      removed = true;
                  }
           if (!removed)
              break;
       }
        word[K] = "";
        preCalc();
        cout << reconstruct(K,0) << endl;
    }
    
    return 0;
}
