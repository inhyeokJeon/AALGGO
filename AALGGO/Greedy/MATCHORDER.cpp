//
//  MATCHORDER.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/17.
//


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

ifstream fin("MATCHORDER.txt");
int N; //선수의수
int match(const vector<int>& korea, const vector<int>& russia){
    int count =0;
    multiset<int> ratings(korea.begin(), korea.end());
    for(int rus =0; rus<N; rus++){
        if(*ratings.rbegin() < russia[rus]){
            ratings.erase(ratings.begin());
        }
        else{
            ratings.erase(ratings.lower_bound(russia[rus]));
            count++;
        }
    }
    return count;
}
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int Test = 0; Test < test_case; Test++){
        fin>>N;
        vector<int> korea;
        vector<int> russia;
        for(int i=0; i<N; i++){
            int rus;
            fin >> rus;
            russia.push_back(rus);
        }
        for(int i = 0; i<N; i++){
            int kor;
            fin >> kor;
            korea.push_back(kor);
        }
        
        cout << match(korea,russia) << endl;
    }
    return 0;
}
