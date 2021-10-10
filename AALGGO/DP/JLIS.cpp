//
//  JLIS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/21.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <limits>
using namespace std;

ifstream fin("JLIS.txt");
int cache[101][101];
int sequence1[101], sequence2[101];
int num1, num2;
const long long NEGINF = numeric_limits<long long>::min();

int LIS(int a, int b){
    int &ret = cache[a+1][b+1];
    if(ret != -1) return ret;
    ret = 0;
    long long A = (a==-1 ? NEGINF : sequence1[a]);
    long long B = (b==-1 ? NEGINF : sequence2[b]);
    long long maxElement = max(A,B);
    for(int i = a + 1; i < num1; ++i){
        if(maxElement < sequence1[i])
            ret = max(ret, LIS(i,b) + 1);
    }
    for(int i = b + 1; i < num2; ++i){
        if(maxElement < sequence2[i])
            ret = max(ret, LIS(a,i) + 1);
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        fin >> num1;
        fin >> num2;
        memset(cache,-1,sizeof(cache));
        memset(sequence1,-1,sizeof(sequence1));
        memset(sequence2,-1,sizeof(sequence2));
        for(int j=0; j< num1; j++){
            fin >> sequence1[j];
        }
        for(int k=0; k<num2; k++){
            fin >> sequence2[k];
        }
        cout << LIS(-1,-1) << endl;
    }
    return 0;
}
