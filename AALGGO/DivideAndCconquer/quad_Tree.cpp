//
//  quad_Tree.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/07/22.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;
ifstream fin("quad.txt");

string quad(string::iterator &str){
    char head = *str;
    ++str;
    
    if( head == 'b' || head == 'w'){
        return string(1,head);
    }
        string upper_left = quad(str);
        string upper_right = quad(str);
        string lower_left = quad(str);
        string lower_right = quad(str);
        return string("x") + lower_left + lower_right + upper_left + upper_right;
    
}
int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    string input;
    
    for (int i=0; i< Test_case ; i++){
        fin >> input;
        //getline(fin, input);
        string::iterator it = input.begin();
        string result = quad(it);
        cout << result << endl;
    }
    return 0;
}
