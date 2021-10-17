//
//  BLOCKGAME.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/13.
//

#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
using namespace std;

ifstream fin("BLOCKGAME.txt");
vector<int> moves;
inline int cell(int y, int x){ return 1 << (y*5 + x); }
void preCalc(){
    //ㄱ 자 모양
    for(int y=0; y<4; y++){
        for(int x=0; x<4; x++){
            vector<int> cells;
            for(int dy=0; dy<2; dy++){
                for(int dx =0 ; dx<2; dx++){
                    cells.push_back(cell(y+dy,x+dx));
                }
            }
            int squares = cells[0] + cells[1] +cells[2] +cells[3];
            for(int i=0; i< 4; i++){
                moves.push_back(squares - cells[i]);
            }
        }
    }
    //1자 모양
    for(int i=0; i<5; i++){
        for(int j=0; j<4; j++){
            moves.push_back(cell(i,j)+cell(i,j+1));
            moves.push_back(cell(j,i)+cell(j+1,i));
        }
    }
}
char cache[1<< 25];
// 현재 게임판 상태가 board일때 현재 차례인 사람이 승리할지 여부를 반환한다.
// (y,x) 칸에 블록이 있다. <=> (y*5 +x) 번 비트가 있다.
int play(int board){
    char &ret = cache[board];
    if(ret!= -1) return ret;
    ret = 0;
    for(int i=0; i< moves.size(); i++){
        //이 수를 게임판에 놓을 수 있는가.
        if((moves[i] & board) == 0){
            // 다음수를 못 놓는다면
            if(!play(board | moves[i])){
                ret = 1;
                break;
            }
        }
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int i = 0; i < test_case; i++){
        preCalc();
        memset(cache, -1, sizeof(cache));
        char space=0;
        int board=0;
        for(int j=0; j<5; j++){
            for(int k=0; k<5; k++){
                fin >> space;
                if(space =='#'){
                    board |= cell(j,k);
                }
                
            }
        }
        
        cout << (play(board) ? "WINNING" : "LOSING") << endl;
    }
    return 0;
}
