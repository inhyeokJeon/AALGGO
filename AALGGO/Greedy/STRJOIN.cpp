//
//  STRJOIN.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/19.
//


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int N;
const int MAX_N = 100;
int length[MAX_N+1];

ifstream fin("STRJOIN.txt");
int print_minimum(){
    priority_queue<int, vector<int>, greater<int> > pq;
    int result = 0;
    for(int i=0; i<N; i++){
        pq.push(length[i]);
    }
    while(pq.size()>1){
        int min_first=pq.top();
        pq.pop();
        int min_second=pq.top();
        pq.pop();
        int temp = min_first+min_second;
        pq.push(temp);
        result += temp;
    }
    return result;
    
}

int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int Test = 0; Test < test_case; Test++){
        fin>>N;
        for(int i=0; i<N; i++){
            fin >> length[i];
        }
        
        cout << print_minimum() << endl;
    }
    return 0;
}

