#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <fstream>
using namespace std;

ifstream fin("DUATHLON2.txt");
const int MAX = 20;
 
int N; //number of contestors
int track; //트랙길이
double runSpeed[MAX], cycleSpeed[MAX]; //뛰는 속도, 자전거 타는 속도
 
//달리기 구간의 길이가 run일 때, i번 선수가 걸린 시간
double time(int i, double run)
{
        double cycle = track - run;
        return run / runSpeed[i] + cycle / cycleSpeed[i];
}
 
//달리기 구간 길이가 run일 때, others(run)-cheater(run) 반환
//이 때, others(run)은 cheater를 제외한 선수들 중 제일 빠른 사람
double difference(double run)
{
        double cheater = time(N - 1, run);
        double others = time(0, run);
        for (int i = 1; i < (N - 1);i++)
               others = min(others, time(i, run));
        return others - cheater;
}
 
//difference() 함수의 최대치의 위치를 삼분 검색으로 계산
double maxDifference(void)
{
        double low = 0, high = track;
        for (int iter = 0; iter < 100; iter++)
        {
               double a = (2 * low + high) / 3; // 1/3 지점
               double b = (low + 2 * high) / 3; // 2/3 지점
               //오목함수에서 최대점 왼쪽에서는 순증가, 최대점 오른쪽에서는 순감소
               if (difference(a) > difference(b))
                       high = b;
               else
                       low = a;
        }
        return (low + high) / 2;
}
 
int main(void)
{
        while(fin >> track)
        {
               fin >> N;
 
               //속도 입력.
               for (int i = 0; i < N; i++)
                       fin >> runSpeed[i] >> cycleSpeed[i];
 
               double run = maxDifference(); //달린 길이
               double cycle = track - run; //자전거 길이
               double timeDiff = difference(run);
               if (timeDiff >= 0.0)
               {
                       cout << fixed << setprecision(0);
                       cout << "The cheater can win by " << (timeDiff * 3600);
                       cout << fixed << setprecision(2);
                       cout << " seconds with r = " << run << "km and k = " << cycle << "km." << endl;
               }
               else
                       cout << "The cheater cannot win." << endl;
        }
        return 0;
}

