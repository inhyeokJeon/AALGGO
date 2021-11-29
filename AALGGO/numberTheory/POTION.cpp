//
//  POTION.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/13.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
ifstream fin("POTION.txt");

int n;
/*
 recipe 의 최대 공약수를 구해라.
 */
int gcd(int p, int q){
    return q==0 ? p : gcd(q,p%q);
}
int ceil(int a, int b){
    return (a + b - 1) / b;
}
vector<int> solve(const vector<int> &recipe, const vector<int> &puts){
    // 최대 공약수를 구한다.
    int b = recipe[0];
    for(int i=1; i<n; i++){
        b = gcd(b, recipe[i]);
    }
    // a = 레시피에 비해 가장 많이 들어있는 재료비율 -> 기준
    int a = b;
    for(int i=0; i<n; i++){
        a = max(a, ceil(b*puts[i],recipe[i]));
    }
    vector<int> ret(n);
    // 더 넣어야할 양을 ret 컨테이너에 추가.
    for(int i=0; i<n; i++){
        ret[i] = a*(recipe[i]/b) - puts[i];
    }
    return ret;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        fin >> n;
        vector<int> recipe(n);
        vector<int> puts(n);
        int temp=0;
        for(int i=0; i<n; i++){
            fin >> recipe[i];
        }
        for(int i=0; i<n; i++){
            fin >> puts[i];
        }
        vector<int> result = solve(recipe, puts);
        for(int i=0; i<result.size(); i++){
            cout << result[i] << " ";
        }
        cout << endl;
        recipe.clear();
        puts.clear();
    }
}
