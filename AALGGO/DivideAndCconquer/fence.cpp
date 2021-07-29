//
//  fence.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/07/29.
//


#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
ifstream fin("fence.txt");
int N;
vector<int> vec;
int fence(int left, int right){
    if(left == right) return vec[left];
    int mid = (left+right)/2;
    // left
    int ret = max(fence(left, mid), fence(mid+1, right));
    // right
    int lo = mid;
    int hi = mid+1;
    int height = min(vec[lo], vec[hi]);
    ret = max(ret, height*2);
    while(left < lo || hi < right ){
        if(hi < right && (lo == left || vec[lo-1] < vec[hi+1])){
            hi ++ ;
            height = min(height, vec[hi]);
        }
        else{
            lo-- ;
            height = min(height, vec[lo]);
        }
        ret = max(ret, height*(hi-lo + 1));
    }
    return ret;
}
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    
    for (int i=0; i< Test_case ; i++){
        fin >> N;
        for(int i=0; i< N; i++){
            int temp;
            fin >> temp;
            vec.push_back(temp);
        }
        cout << fence(0, N-1) << endl;
        vec.clear();
    }
    return 0;
}

