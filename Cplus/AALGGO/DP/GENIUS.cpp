//
//  GENIUS.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/14.
//


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("GENIUS.txt");

int N; // MP3 플레이어에 들어 있는 곡의 수 1<= <=50
int K; // K 분 30초 의 1<= <=1000000
int M; // 태윤이가 좋아하는 곡의 수 1<= <=10
int L[51]; // N개의 곡의 길이 1<= <=4;
double T[51][51]; // i번 곡이 끝난 뒤 j번 곡이 재생할 확률

class Matrix{
private:
    vector<vector <double> > v;
    int m_size;
public:
    Matrix(int n, vector<vector<double >> v2) : m_size(n){
        v.resize(m_size, vector<double>(m_size,0));
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                v[i][j] = v2[i][j];
            }
        }
    };
    Matrix(int n) : m_size(n){
        v.resize(m_size, vector<double>(m_size,0));
    };
    
    Matrix Identity(){
        Matrix result(m_size);
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                if(i==j) result.v[i][j] = 1;
                else result.v[i][j] = 0;
            }
        }
        return result;
    };
    
    Matrix operator*(Matrix &M){
        Matrix result(m_size);
        for(int i=0; i< m_size; i++){
            for(int j=0; j< m_size; j++){
                for(int k=0; k< m_size; k++){
                    result.v[i][j] += (v[i][k] * M.v[k][j]);
                }
            }
        }
        return result;
    };
    
    Matrix pow(int k){
        if(k == 0) return Identity();
        Matrix result(m_size);
        // 홀
        if(k % 2 == 1) return pow(k-1)**this;
        Matrix half = pow(k/2);
        return half*half;
    };
    
    double *operator[](int i){
        return &v[i][0];
    }
    
    void PrintMatrix(){
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                cout << v[i][j] << " ";
            }
            cout << endl;
        }
    }
};

vector<double> getProb2(){
    //start(time-3, 0) ~ start(time-3, N-1)
    //start(time-2, 0) ~ start(time-2, N-1)
    //start(time-1, 0) ~ start[time-1, N-1)
    //start(time  , 0) ~ start(time  , N-1).
    Matrix W(N*4);
    // 첫 3*n의 원소는 그대로 복사해 온다.
    // 이해가 정말 안됬는데 이렇게 하니 좀 되었음..
    // NOOX start(time-3) -> (time-2 + time-1 + time)
    // NNOX start(time-2) -> (time-1 + time);
    // NNNX start(time-1) -> (time);
    // XXXX start(time  ) -> (time분 후 곡이 불러질 확률을 구한다. T를 이용해서 );
    for(int i=0; i<3*N; i++)
        W[i][i+N] = 1.0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            W[3*N+i][(4-L[j])*N +j] = T[j][i];
        }
    }
    Matrix Wk = W.pow(K);
    
    vector<double> result(N);
    //song번 노래가 재생되고 있을 모두 확률을 계산한다.
    for(int song=0; song<N; song++){
        //song 번 노래가 시작했을 시간을 모두찾아 결과에 저장한다.
        for(int start=0 ; start<L[song] ; start++){
            result[song] += Wk[(3-start)*N + song][3*N];
        }
    }
    return result;
    
}
int main(int argc, const char * argv[]) {
    int test_case;
    fin >> test_case;
    
    for(int i = 0; i < test_case; i++){
        fin >> N >> K >> M;
        for(int j=0; j<N; j++){
            fin >> L[j];
        }
        for(int j=0; j<N; j++){
            for(int k=0; k<N; k++){
                fin >> T[j][k];
            }
        }
        
        vector<double> result = getProb2();
        for(int j=0; j<M; j++){
            int Song;
            fin >> Song;
            printf("%.8f ",result[Song]);
            
        }
        cout << endl;
    }
    return 0;
}
