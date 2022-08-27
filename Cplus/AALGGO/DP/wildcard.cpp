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
using namespace std;

ifstream fin("wildcard.txt");

bool check(const string& wildcard, const string& filename){
    int pos = 0;
    while(pos < wildcard.size() && pos < filename.size() &&
          (wildcard[pos]=='?' || (wildcard[pos] ==filename[pos] ))){
        pos ++;
    }
    if(pos == wildcard.size()){
        return pos==filename.size();
    }
    if (wildcard[pos] == '*'){
        for(int i=0; i+pos <= filename.size(); ++i){
            if(check(wildcard.substr(pos+1), filename.substr(i+pos)))
                return true;
        }
    }
    return false;
}

void wild(string wildcard, vector<string>& filename){
    vector<string> result;
    for(int i=0; i<filename.size(); i++){
        if(check(wildcard, filename[i])){
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
