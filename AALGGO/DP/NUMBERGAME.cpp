//
//  NUMBERGAME.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/12.
//

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("NUMBERGAME.txt");
int n; // 테스트판의 길이.
int cache[50][50];
int board[50];
const int MIN = -50001;
// 왼쪽 1개 가져갈때.
// 오른쪽 1개 가져갈때.
// 왼쪽 두개 없앨때
// 오른쪽 두개 없앨떄
void preCalc(){
    for(int i=0; i< 50; i++){
        for(int j=0; j<50; j++){
            cache[i][j] = MIN;
        }
    }
}

int play(int left, int right){
    if(left > right) return 0;
    int &ret = cache[left][right];
    if(ret!= MIN) return ret;
    // 수를 가져가는 경우
    ret = max(board[left] - play(left+1, right), board[right] - play(left, right-1));
    //수를 없애는 경우
    if(right -left +1 >= 2){
        ret = max(ret, -play(left+2, right));
        ret = max(ret, -play(left, right-2));
    }
    
    return ret;
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int i = 0; i < test_case; i++){
        fin >> n;
        preCalc();
        memset(board, -1, sizeof(board));
        for(int j=0; j<n; j++){
            fin >> board[j];
        }
        cout << play(0, n-1) << endl;
    }
    return 0;
}
