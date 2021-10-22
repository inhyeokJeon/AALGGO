//
//  unordered_set.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/22.
//

#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int main() {
    unordered_set<string> s;
    s.insert("inhyeok");
    s.insert("korea");
    s.insert("tiger");
    s.insert("hello");
    s.insert("yundu");
    s.insert("test");
    s.insert("test");
    for (const auto& elem : s) {
      std::cout << elem << std::endl;
    }
}
