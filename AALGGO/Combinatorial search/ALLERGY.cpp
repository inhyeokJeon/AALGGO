//
//  ALLERGY.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/01.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
ifstream fin("ALLERGY.txt");

int friendNum;
int foodNum;
// i번 친구가 먹을 수 있는 음식의 집합
vector<int> canEat[50];
// i번 음식을 먹을 수 있는 친구들의 집합
vector<int> eaters[50];
const int INF = 987654321;
int best;
void clear();

// edible 지금까지 고른 음식중, i 번 친구가 먹을 수 있는 음식의 수
// chosen : 지금까지 선택한 음식의 수
void search(vector<int> &edible, int chosen){
    if(chosen >= best ) return;
    int first = 0; // 아직 음식이 없는 첫번째 친구
    while(first < friendNum && edible[first] > 0) first++;
    if(first ==friendNum){
        best = chosen;
        return;
    }
    // 음식이 없는 친구의 음식 순회
    for(int i=0; i< canEat[first].size(); i++){
        int food = canEat[first][i];
        for(int j=0; j<eaters[food].size(); j++){
            edible[eaters[food][j]]++;
        }
        search(edible, chosen + 1);
        for(int j=0; j<eaters[food].size(); j++){
            edible[eaters[food][j]]--;
        }
    }
    
}

int main(){
    int test_case;
    fin >> test_case;
    for(int test =0; test<test_case; test++){
        best = INF;
        fin >> friendNum >> foodNum;
        map<string, int> index;
        for(int i=0; i< friendNum; i++){
            string name;
            fin >> name;
            index[name] = i;
        }
        for(int i=0; i<foodNum; i++){
            int num;
            fin >> num;
            for(int j=0; j<num; j++){
                string temp;
                fin >> temp;
                eaters[i].push_back(index[temp]);
                canEat[index[temp]].push_back(i);
            }
        }
        vector<int> edible(friendNum,0);
        search(edible,0);
        cout << best << endl;
        clear();
    }
    
}

void clear(){
    for(int i=0; i<friendNum; i++){
        canEat[i].clear();
    }
    for(int i=0; i<foodNum; i++){
        eaters[i].clear();
    }
}
