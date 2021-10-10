//
//  PI.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/21.
//

#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <cstring>

using namespace std;

ifstream fin("pi.txt");

int cache[10001];

string S;
bool first(int start, int end){
    char fisrt_char = S[start];
    for(int index = start+1; index<= end; index++){
        if(fisrt_char!=S[index])
            return false;
    }
    return true;
}
bool second(int start, int end){
    int prev_difference = S[start+1]-S[start];
    for(int index = start+1; index< end; index++){
        int difference = S[index+1]-S[index];
        if(abs(difference) != 1 || prev_difference != difference) return false;
    }
    return true;
}
bool third(int start, int end){
    char first = S[start];
    char second = S[start+1];
    for(int index = start+2; index<= end; index++){
        if((index % 2)  == (start % 2) ){
            if (S[index] != first) return false;
        }
        else if ((index % 2)  == ((start+1) % 2) ){
            if (S[index] != second)
                return false;
        }
    }
    return true;
}
bool forth(int start, int end){
    int prev_difference = S[start+1]-S[start];
    for(int index = start+1; index< end; index++){
        int difference = S[index+1]-S[index];
        if(prev_difference != difference) return false;
    }
    return true;
}
int difficulty(int start, int end){
    // 모든 숫자가 같을때
    if(first(start, end)){
        return 1;
    }
    // 숫자가 1씩 단조 증가하거나 감소할 때
    else if(second(start, end)){
        return 2;
    }
    // 두 숫자가 번갈아가며 나타날 때
    else if (third(start, end))
        return 4;
    // 숫자가 모두 등차 수열일 때
    else if (forth(start, end))
        return 5;
    // 이 외 에브리띵
    return 10;
}

int pi(int position){
    if(position == S.size()) return 0;
    int &ret = cache[position];
    if(ret != -1) return ret;
    ret = 999999999;
    for(int i=3; i<=5; i++){
        if(position + i <=S.size() )
            ret = min(ret, pi(position + i)+ difficulty(position, position + i-1));
    }
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        fin >> S;
        memset(cache,-1,sizeof(cache));
        cout << pi(0) << endl;
    }
    return 0;
}
