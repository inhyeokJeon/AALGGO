//
//  OCR.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/01.
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

int m; // 원문에 출현할 수 있는 단어의 수 (1<=m<=500)
int q; // 처리해야 할 문장의 수 ( 1<=q<=100)
int c; // 분류기로 인식한 문장의 단어의 수;
double B[501]; // 각 단어가 문장의 처음에 출현할 확률. 항상 합은 1
double T[501][501]; // T[i][j] i번 단어의 다음 단어가 j번 단어일 확률. 항상 합은 1
double M[501][501]; // M[i][j] i번 단어가 적힌 조각을 j번 단어로 분류할 확률. 항상 합은 1
int choice[102][502]; // 선택
double cache[102][502]; // 메모이제이션 1로 초기화
int R[100]; // 분류기가 반환한 문장, 단어 번호로 되어 있음.
string word[501];
ifstream fin("OCR.txt");

// Q[segment] 이후를 채워서 얻을 수 있는 최대 g() 곱의 로그 값을 반환한다.
// Q[segment-1] == previousMatch 라고 가정한다.
double recognize(int segment, int previousMatch){
    // 기저사례
    if(segment == c) return 0;
    double &ret = cache[segment][previousMatch];
    if(ret != 1.0) return ret;
    ret = -1e200; // log(0) = 음의 무한대에 해당하는 값;
    int &choose = choice[segment][previousMatch];
    for( int thisMatch = 1; thisMatch <= m; thisMatch++){
        double cand = T[previousMatch][thisMatch] + M[thisMatch][R[segment]] + recognize(segment+1, thisMatch);
        if( ret < cand){
            ret = cand;
            choose = thisMatch;
        }
    }
    return ret;
}

string reconstruct(int segment, int previousMatch){
    int choose = choice[segment][previousMatch];
    string ret = word[choose];
    if(segment < c-1)
        ret = ret + " " + reconstruct(segment+1, choose);
    return ret;
}


// 캐시 초기화 double 이기 떄문.
void initialize()
{
    for (int i = 0; i < c; i++)
        for (int j = 0; j <= m; j++) {
            cache[i][j] = 1.0;
        }
}

int main(int argc, const char * argv[]) {
    fin >> m;
    fin >> q;
    for(int j = 1; j <= m; j++){
        fin >> word[j];
    }
    for(int j = 1; j <= m; j++){
        fin >> B[j];
        B[j] = log(B[j]);
    }
    for(int j = 0; j <= m ; j++){
        for(int k = 1; k <= m ; k++){
            // Q[-1]이 항상 이 시작의 단어라고 지정한다.
            // B(Q[0]) = T([Q[-1], Q[0]) 를 이용한다.
            if(j==0)
                T[j][k] = B[k];
            else{
                fin >> T[j][k];
                T[j][k] = log(T[j][k]);
            }
        }
    }
    for(int j = 1; j <= m ; j++){
        for(int k = 1; k <= m ; k++){
            fin >> M[j][k];
            M[j][k] = log(M[j][k]);
        }
    }
    
    for(int j = 0; j < q; j++){
        fin >> c;
        initialize();
        for(int k = 0; k < c; k++){
            string input;
            fin >> input;
            for(int l = 1; l<=m; l++){
                if(input == word[l]){
                    R[k] = l;
                    break;
                }
            }
        }
        
        recognize(0,0);
        cout << reconstruct(0,0) << endl;
    }
    
    
    return 0;
}
