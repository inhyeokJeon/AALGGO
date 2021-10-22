//
//  BOARDCOVER.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/02.
//

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int H, W =0;
ifstream fin("test_boardcover.txt");
const int cover[4][3][2] ={
    {{0,0}, {0,1}, {1,0}},
    {{0,0}, {0,1}, {1,1}},
    {{0,0}, {1,0}, {1,1}},
    {{0,0}, {1,-1}, {1,0}}
};
// first ( x,y ) ( x+1,y ) ( x+1,y+1)

bool set(vector<vector <int > >& board, int x, int y , int type, int delta){
    bool ok = true;
    for(int i=0; i< 3; i++){
        const int temp_x = x + cover[type][i][1];
        const int temp_y = y + cover[type][i][0];
        if( temp_y <0 || temp_y >=board.size() || temp_x<0 || temp_x >= board[0].size() ){
            ok = false;
        }
        else if((board[temp_y][temp_x] +=delta ) > 1){
            ok = false;
        }
    }
    return ok;
}

void reset(vector<vector <int > > board,int x, int y,int type){
    for(int i=0; i< 3; i++){
        int temp_x = x + cover[type][i][1];
        int temp_y = y + cover[type][i][0];
        board[temp_y][temp_x] = 0;
        
    }
}
void set_1(vector<vector <int > > board, int x, int y,int type){
    for(int i=0; i< 3; i++){
        int temp_x = x + cover[type][i][1];
        int temp_y = y + cover[type][i][0];
        board[temp_y][temp_x] = 1;
    }
}


int boardcover (vector<vector <int> >& board){
    int y = -1, x = -1;
    for(int i=0; i< H; i++){
        for(int j=0; j<W; j++){
            if(board[i][j]==0){
                y = i;
                x = j;
                break;
            }
        }
        if(y != -1) break;
    }
    if( y == -1){
        return 1;
    }
    int ret=0;
    for(int i=0; i<4; i++){
        if(set(board, x, y, i,1)){
            ret+= boardcover(board);
        }
        set(board, x,y,i,-1);
    }
    return ret;
}
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    for (int i=0; i< Test_case ; i++){
        fin >> H >> W;
        vector<vector <int> > board;
        int count = 0;
        char temp;
        for(int i = 0 ; i<H; i++){
            vector<int> small_board;
            for(int j=0; j<W; j++){
                fin >> temp;
                if(temp == '.'){
                    small_board.push_back(0);
                    count ++;
                }
                else if (temp =='#'){
                    small_board.push_back(1);
                }
            }
            board.push_back(small_board);
        }
        if(count % 3 != 0)
            cout << 0 << endl;
        else
            cout << boardcover(board) << endl;
        
    }
    return 0;
}
