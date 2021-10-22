//
//  LUNCHBOX.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/18.
//


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

int N;
const int MAX_N = 10000;
int e[MAX_N+1];
int m[MAX_N+1];

ifstream fin("LUNCHBOX.txt");
int lunchbox(){
    int total_E=0, result=0;
    vector<pair<int, int>> vec;
    for(int i=0; i<N; i++){
        vec.push_back(make_pair(-e[i],i));
    }
    sort(vec.begin(), vec.end());
    for(int i=0; i<N; i++){
        int box = vec[i].second;
        total_E += m[box];
        result = max(result, total_E + e[box]);
    }
    
    return result;
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int Test = 0; Test < test_case; Test++){
        fin>>N;
        vector<int> korea;
        vector<int> russia;
        for(int i=0; i<N; i++){
            fin >> m[i];
        }
        for(int i = 0; i<N; i++){
            fin >> e[i];
        }
        
        cout << lunchbox() << endl;
    }
    return 0;
}

