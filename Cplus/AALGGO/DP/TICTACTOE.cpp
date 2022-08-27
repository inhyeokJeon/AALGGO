//
//  TICTACTOE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/12.
//


#include <iostream>
#include <fstream>
#include <string> // string
#include <vector>
using namespace std;

ifstream fin("TICTACTOE.txt");

//cache 를 -2 로 리셋
// 3^9 = 19683;
int cache[19683];

void preCalc(){
    for(int i=0; i<19683 ; i++){
        cache[i] = -2;
    }
}

//turn 이 한줄을 만들었는지 판단한다.
bool isFinished(const vector<string>& board, char turn){
    // 가로중에 세개가 turn 이랑똑같을때
    for(int i=0; i<3; i++){
        if ( board[i][0] == turn && board[i][1] ==turn && board[i][2] == turn) return true;
    }
    //세로
    for(int i=0; i<3; i++){
        if( board[0][i] == turn && board[1][i] == turn && board[2][i] == turn) return true;
    }
    // 대각선 1시에서 7시
    if(board[0][0] == turn && board[1][1] == turn && board[2][2] == turn) return true;
    // 대각서 11시에서 5시
    if(board[0][2] == turn && board[1][1] == turn && board[2][0] == turn) return true;
    
    return false;
}


// 틱택토 게임판이 주어질 때 [0, 19682] 범위의 정수로 변환한다.
int bijection(const vector<string>& board){
    int ret =0;
    for(int i=0; i< 3; i++){
        for(int j=0; j<3; j++){
            ret = ret * 3;
            if(board[i][j] == 'o') ret++;
            else if(board[i][j] == 'x') ret += 2;
        }
    }
    return ret;
}

// 이기면 1 비기면 0 지면 -1
int canWin(vector<string>& board, char turn){
    //기저 사례 다음턴이 이기면 짐
    if(isFinished(board, 'o'+'x'-turn)) return -1;
    int &ret = cache[bijection(board)];
    if(ret!=-2) return ret;
    // 모든 반환값의 미니멈 -2
    int minValue = 2;
    // 보드판에 비어있을때.
    for(int y=0; y<3; y++){
        for(int x=0; x<3; x++){
            if(board[y][x] == '.'){
                board[y][x] = turn;
                minValue = min(minValue, canWin(board,'o'+'x'-turn)); // 다음턴에 상대가 이기든지 지든지.
                board[y][x] = '.';
            }
        }
    }
    // 더이상 플레이 할 수 없거나 지는것이 최선일 경우
    if(minValue==2 || minValue==0) return ret = 0;
    // 최선이 상대가 이기는 거라면 난 무조건 지고, 상대가 지는 거라면 난 이긴다.
    return ret = -minValue;
}


int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    vector<string> board;
    for(int i = 0; i < test_case; i++){
        board.clear();
        int checkturn = 0;
        for(int j=0; j< 3; j++){
            string temp;
            fin >> temp;
            for(int k=0; k<3; k++){
                if(temp[k] != '.') checkturn++;
            }
            board.push_back(temp);
        }
        char turn = 'x';
        if( checkturn % 2 == 1) turn = 'o';
        preCalc(); // -2로 캐시 초기화
        int result = canWin(board, turn);
        switch(result){
            case -1: // 지면
                cout << (char)('o'+'x'-turn) << endl;
                break;
            case 0: // 비기면
                cout << "TIE" << endl;
                break;
            case 1: // 이기면
                cout << turn << endl;
                break;
        }
        
    }
    return 0;
}
