//
//  wildcard.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/14.
//
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstring>

using namespace std;

ifstream fin("wildcard.txt");
string W,F;
int cache[101][101];
bool check(int w, int f){
    int &ret = cache[w][f];
    if(ret!=-1) return ret;
    while(w < W.size() && f < F.size() &&
          (W[w]=='?' || (W[w] ==F[f] ))){
        w++;
        f++;
    }
    
    if(w == W.size()){
        return ret = (f==F.size());
    }
    
    if (W[w] == '*'){
        for(int i=0; i+f <= F.size(); i++){
            if(check(w+1, i+f))
                return ret=1;
        }
    }
    return ret = 0;
}

void wild(string wildcard, vector<string>& filename){
    vector<string> result;
    W = wildcard;
    for(int i=0; i<filename.size(); i++){
        memset(cache, -1, sizeof(cache));
        F = filename[i];
        if(check(0, 0)){
            result.push_back(filename[i]);
        }
    }
    sort(result.begin(), result.end());
    for(int i=0; i<result.size(); i++){
        cout << result[i] << endl;
    }
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        string wildcard;
        int num;
        fin >> wildcard;
        fin >> num;
        vector<string> filename;
        
        for(int j=0; j<num; j++){
            string temp;
            fin >> temp;
            filename.push_back(temp);
        }
        wild(wildcard, filename);
    }
    return 0;
}
