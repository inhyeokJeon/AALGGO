//
//  main.cpp
//  AALGGO
// next_permutation
//  Created by inhyeok on 2021/07/15.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    cout << "Hello, World!\n";
    vector <int> a;
    a.push_back(7);
    a.push_back(5);
    a.push_back(2);
    a.push_back(1);
    a.push_back(10);
    int arr[5] = {1,2,3,5,2};
    //fill(a.begin(), a.end(), 0);
    sort(a.begin(), a.end(), true);
    /*
    do {
        for(int i=0; i < a.size(); i++){
            cout << a[i] << " ";
        }
        cout << endl;
    } while(prev_permutation(a.begin(), a.end()));
    */
    for(int i=0; i< 5; i++){
        cout << a[i] << " ";
    }
    return 0;
}
