//
//  sopung.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/07/15.
//

#include <iostream>
#include <fstream>

using namespace std;
int N, couple;
bool friends[10][10];


ifstream fin("test_sopung.txt");

int factorial(int a){
    if(a == 1 || a == 0)
        return 1;
    else
        return (a * (factorial(a-1)));
}
// reset array info
void reset_friend(void)
{
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            friends[i][j] = false;
        }
    }
}
int check(bool arr[]){
    int first_free = -1;
    for(int i=0; i<N; i++){
        if(!arr[i]){
            first_free = i;
            break;
        }
    }
    if(first_free==-1){
        return 1;
    }
    int ret=0;
    
    for(int i=first_free+1; i<N; i++){
        if(friends[first_free][i] && !arr[i]){
            arr[first_free] = true;
            arr[i] = true;
            ret += check(arr);
            arr[first_free]= false;
            arr[i] = false;
        }
    }
    
    
    return ret;
}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    cout << "Test_Case : " << Test_case << endl;
    for (int i=0; i< Test_case ; i++){
        fin >> N >> couple;
        int x,y;
        bool exist_friend[10]={false,};
        reset_friend();
            
        for(int i=0; i<couple; i=i+1){
            fin >> x >> y;
            friends[x][y] = true;
            friends[y][x] = true;
        }
        int ret = check(exist_friend);
        cout<< "test_case # "<< i+1 << " : " << ret << endl;
    }
     
    return 0;
}
