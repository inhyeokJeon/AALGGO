//
//  QUANTIZE.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/09/23.
//


#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;

ifstream fin("QUANTIZE.txt");
int cache[100][10];
int n;

int arr[100];
int pSum[100]; // 부분 합 arr[0] + ... arr[i]
int pSqSum[100]; // 제곱근 부분 합 arr[0]^2+...arr[i]^2
const int INF = 987654321;

// 정렬 하고 부분합들 계산하는 함수.
void precalc(){
    sort(arr, arr+n);
    pSum[0] = arr[0];
    pSqSum[0] = arr[0] * arr[0];
    for(int i =1; i<n; i++){
        pSum[i] = pSum[i-1] + arr[i];
        pSqSum[i] = pSqSum[i-1] + (arr[i] * arr[i]);
    }
}

// arr[low]...arr[high] 구간을 하나의 숫자로 표현할 때 최소 오차 합 계산
int minDiffrence(int low, int high)
{
    // 부분합을 이용해 arr[low]...arr[high]의 합 구함
    int sum = pSum[high] - (low == 0 ? 0 : pSum[low - 1]);
    int squareSum = pSqSum[high] - (low == 0 ? 0 : pSqSum[low - 1]);
    //평균을 반올림한 값으로 이 수들을 표현
    int mean = (int)(0.5 + (double)sum / (high - low + 1)); //반올림
    // sum(arr[i]-mean)^2를 전개한 결과를 부분합으로 표현
    // ∑(arr[i]-mean)^2 = (high-low+1)*mean^2 - 2*(∑arr[i])*mean + ∑arr[i]^2
    int result = squareSum - (2 * mean*sum) + (mean*mean*(high - low + 1));
    return result;
}



int QUANT(int from, int parts){
    //기저 사례:모든 숫자를 다 양자화했을 때
    if (from == n)
           return 0;
    //기저 사례 : 숫자는 아직 남았는데 더 묶을 수 없을 때 아주 큰 값 반환
    if (parts == 0)
           return INF;
    int &result = cache[from][parts];
    if (result != -1)
           return result;
    result = INF;
    //조각의 길이를 변화시켜 가며 최소치 찾음
    for (int partSize = 1; from + partSize <= n; partSize++)
           result = min(result, minDiffrence(from, from + partSize - 1) + QUANT(from + partSize, parts - 1));
    return result;

}

int main(int argc, const char * argv[]) {
    int Test_case;
    fin >> Test_case;
    
    for (int i=0; i< Test_case ; i++){
        int s;
        fin >> n;
        fin >> s;
        
        memset(cache,-1,sizeof(cache));
        for(int j=0; j<n; j++){
            fin >> arr[j];
        }
        precalc();
        cout << QUANT(0,s) << endl;
    }
    return 0;
}

