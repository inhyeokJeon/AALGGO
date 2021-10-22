//
//  clocksync.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/03.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
const int INF = 9999;

ifstream fin("test_clock.txt");
int clock_list[10][16] = {
    {1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0}, //0
    {0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0},//1
    {0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1},//2
    {1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0},//3
    {0,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0},
    {1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1}, // 5
    {0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1},
    {0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1},// 7
    {0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},
    {0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0} //9
};

void push(vector<int> &table, int button){
    for(int i=0; i<16; i++){
        if(clock_list[button][i]==1){
            table[i] += 3;
            if(table[i] == 15){
                table[i] = 3;
            }
        }
    }
}
bool areAligned(const vector<int> & table){
    for(int i=0; i< 16; i++){
        if(table[i] != 12){
            return false;
        }
    }
    return true;
}
int clock(vector<int> &table, int button){
    if(button == 10){
        return areAligned(table) ? 0 : INF;
    }
    int ret = INF;
    for( int i=0; i<4; i++){
        ret = min(ret, i + clock(table, button+1));
        push(table,button);
    }
    
    return ret;
}
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    for (int i=0; i< Test_case ; i++){
        vector<int> arr(16, 0);
        for(int j = 0 ; j< 16; j++){
            fin >> arr[j];
            
        }
        if(clock(arr,0) == 9999){
            cout << -1 << endl;
        }
        else{
            cout << clock(arr,0) << endl;
        }
        
    }
    return 0;
}
