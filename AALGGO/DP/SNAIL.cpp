//
//  SNAIL.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/28.
//

#include <iostream>
#include <fstream>
using namespace std;
int n,m;
ifstream fin("SNAIL.txt");
double cache[1000][2000];
 
double snail(int days, int distance){
    if( days == m ) return distance >= n ? 1 : 0;
    double &ret = cache[days][distance];
    if(ret !=-1.0 ) return ret;
    ret = (0.25*snail(days+1, distance+1)) + (0.75*snail(days+1, distance+2));
    
    return ret;
}
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    for (int i=0; i< Test_case ; i++){
        fin >> n;
        fin >> m;
        for (int i = 0; i < 1000; i++)
            for (int j = 0; j < 2000; j++)
                cache[i][j] = -1.0;
        if( m >= n ){
            cout << 1 ;
        }
        else{
            printf("%.10f", snail(0,0));
            cout << endl;
        }
    }
    return 0;
}
