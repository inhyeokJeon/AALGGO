//
//  fanmeeting.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/06.
//

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

ifstream fin("fan_meeting.txt");

vector<int> karatsuba(vector<int> &a, vector<int> &b){
    
    vector<int> ret;
    return ret;
}

int hugs(const string& members, const string& fans){
    int N = members.size();
    int M = fans.size();
    vector<int> a(N) , b(M);
    for(int i=0; i<N; i++){
        a[i] = (members[i] =='M');
    }
    for(int i=0; i<M; i++){
        b[M-i-1] = (fans[i] =='M');
    }
    vector<int> vec = karatsuba(a,b);
    int result =0;
    for(int i = N-1; i<M; i++){
        if(vec[i] == 0) result++;
    }
    return result;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        string members, fans;
        fin >> members;
        fin >> fans;
        
        cout << hugs(members, fans) << endl;
    }
    return 0;
}
