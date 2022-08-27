//
//  BOARDCOVER2.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/31.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

ifstream fin("BOARDCOVER2.txt");

int BoardHeight;
int BoardWidth;
int BlockHeight;
int BlockWidth;

vector<string> Board;
vector<vector<pair<int ,int> > > rotations;
int blockSize;
int cover[10][10];
int best;

vector<string> rotate(const vector<string> &block){
    vector<string> ret(block[0].size(), string(block.size(),' '));
    for(int i=0; i< block.size(); i++){
        for(int j=0; j < block[0].size(); j++){
            ret[j][block.size()-i-1] = block[i][j];
        }
    }
    return ret;
}

//-----
void Block_preprocesing(vector<string> block){
    rotations.clear();
    rotations.resize(4);
    for(int rotation = 0; rotation<4; rotation++){
        int X = -1, Y = -1;
        for(int i=0 ; i<block.size(); i++){
            for(int j=0; j<block[i].size(); j++){
                if(block[i][j]=='#'){
                    if(Y == -1){
                        Y = i;
                        X = j;
                    }
                    rotations[rotation].push_back(make_pair(i-Y, j-X));
                }
            }
        }
        block = rotate(block);
    }
    sort(rotations.begin(), rotations.end());
    rotations.erase(unique(rotations.begin(), rotations.end()),rotations.end());
    blockSize = rotations[0].size();
}


// todo
// delta
bool set(int y, int x, const vector<pair<int,int>> &block, int delta){
    bool result = true;
    for(int i=0; i< block.size(); i++){
        if(y+block[i].first >=0 && y+block[i].first<BoardHeight && x+block[i].second >=0 && x+block[i].second < BoardWidth){
            cover[y+block[i].first][x+block[i].second] += delta;
            result = result && (cover[y+block[i].first][x+block[i].second] == 1);
        }
        
        else{
            result = false;
        }
         
    }
    return result;
}

bool prune(int placed){
    int cnt = 0;
    
    for(int i=0; i<BoardHeight; i++){
        for(int j=0; j<BoardWidth; j++){
            cnt += (cover[i][j]) ? 0:1;
        }
    }
    
    if((cnt/blockSize) + placed <= best)
        return true;
    else{
        return false;
    }
}

void search(int placed){
    //가지치기
    if(prune(placed))  return;
    // 놓여 지지않은 가장 왼쪽 위 칸을 찾는다.
    int Y = -1, X = -1;
    for(int i=0; i<BoardHeight; i++){
        for(int j=0; j<BoardWidth ; j++){
            if(cover[i][j] == 0){
                Y = i;
                X = j;
                break;
            }
        }
        if(Y != -1) break;
    }
    
    if(Y == -1) {
        best = max(best, placed);
        return;
    }
    
    //cout << placed << endl;
    
    // 이칸을 덮는다.
    for(int i=0; i<rotations.size(); i++){
        if(set(Y,X,rotations[i], 1))
            search(placed+1);
        set(Y,X,rotations[i], -1);
    }
    // 이칸을 막아둔다.
    cover[Y][X] = 1;
    search(placed);
    cover[Y][X] = 0;
    
    
}

int solve(){
    best = 0;
    for(int i=0; i< BoardHeight; i++){
        for(int j=0; j<BoardWidth; j++){
            cover[i][j] = ( Board[i][j] == '#'? 1 : 0 );
        }
    }
    search(0);
    return best;
}




int main(){
    int test_case;
    fin  >> test_case;
    for(int test=0;  test<test_case; test++){
        Board.clear();
        fin >> BoardHeight >> BoardWidth >> BlockHeight >> BlockWidth;
        for(int i=0; i<BoardHeight; i++){
            string board;
            fin >> board;
            Board.push_back(board);
        }
        vector<string> Block;
        for(int i=0; i<BlockHeight; i++){
            string block;
            fin >> block;
            Block.push_back(block);
        }
        Block_preprocesing(Block);
        cout << solve() << endl;
    }
    return 0;
}
