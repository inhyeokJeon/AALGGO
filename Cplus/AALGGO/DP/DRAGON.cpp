//
//  DRAGON.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/11.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <assert.h>
#include <string>

using namespace std;
ifstream fin("DRAGON.txt");

const int MAX = 1000000000 + 1;
int length[51];

int n; // n세대 드래곤 커브
int p; // 문자열의 p 번째 글자부터
int l; // l번쨰 글자 까지.
void precalc(){
    length[0] = 1;
    for(int i=1; i<= 50; i++)
        length[i] = min(MAX, 2*length[i-1] + 2);
}

const string EXPAND_X = "X+YF";
const string EXPAND_Y = "FX-Y";

// Dragon 을 generaion 진화 시킨 상태에서 skip번째 문자열을 출력한다.
char expand(const string& Dragon, int generation, int skip){
    //기저 사례
    if(generation == 0){
        assert(skip < Dragon.size()); // 드래곤 길이 보다 찾으려는 위치가 작으면 종료.
        return Dragon[skip];
    }
    for(int i=0; i< Dragon.size(); i++){
        //문자열이 확장되는 경우
        if(Dragon[i] == 'X' || Dragon[i]== 'Y'){
            if(skip >= length[generation])
                skip -= length[generation];
            else if(Dragon[i]=='X')
                return expand(EXPAND_X, generation-1, skip);
            else
                return expand(EXPAND_Y, generation-1, skip);
        }
        //확장되지 않고 건너 뛰어야 할 경우
        else if(skip>0){
            --skip;
        }
        else
            return Dragon[i];
        
    }
    return '*';
}
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    precalc();
    for(int i = 0; i < test_case; i++){
        fin >> n >> p >> l;
        for(int j=0; j< l; j++)
            cout << expand("FX", n, p+j-1);
        cout << endl;
    }
    
    return 0;
}
