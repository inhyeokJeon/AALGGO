//
//  LOAN.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/11/08.
//
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("LOAN.txt");
// 대출 잔금은 ?
double balance(double amount, int duration, double rates, double monthlyPayment){
    double balance = amount; // 남은 대출금
    for(int i =0; i<duration; i++){
        balance *= (1+ (rates/12)/100.0 ); // 한달에 이자가 붙음.
        balance -= monthlyPayment; // 한달에 이만큼 갚은만큼 뺀다.
    }
    return balance;
}

// 한달에 갚아야할 최소 금액을 리턴
double payment(double amount, int duration, double rates){
    // 한달간 갚아야할 금액을 lo, hi 로 표현;
    // hi = 원금 + 이자.
    double lo = 0, hi = amount*(1+ (rates/12)/100);
    for(int it=0; it<100; it++){
        double mid = (lo+hi)/2.0;
        if(balance(amount,duration,rates,mid)<=0){
            hi = mid;
        }
        else{
            lo = mid;
        }
    }
    return hi;
}
int main(){
    int test_case;
    fin >> test_case;
    for(int test=0; test < test_case; test++){
        double N , P; // N -> 대출 금액, P -> 월 이자(P/12)%
        int M; // 개월수, 갚아야할 M 개월
        fin >> N >> M >> P ;
        printf("%0.10f\n",payment(N,M,P));
    }
}
