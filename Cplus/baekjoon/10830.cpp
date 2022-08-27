//
//  10830.cpp
//  AALGGO
//
//  Created by inhyeok on 2021/10/14.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
ifstream fin("10830_baekjoon.txt");

class Matrix{
private:
    vector<vector <long long> > v;
    int m_size;
public:
    Matrix(int n, vector<vector<long long >> v2) : m_size(n){
        v.resize(m_size, vector<long long>(m_size,0));
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                v[i][j] = v2[i][j];
            }
        }
    };
    Matrix(int n) : m_size(n){
        v.resize(m_size, vector<long long>(m_size,0));
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
                result.v[i][j] %= 1000;
            }
        }
        return result;
    };
    
    Matrix pow(long long k){
        if(k == 0) return Identity();
        Matrix result(m_size);
        // 홀
        if(k % 2 == 1) return pow(k-1)**this;
        Matrix half = pow(k/2);
        return half*half;
    };
    /*
    long long operator[](int i){
        return v[i][0];
    }
    */
    void PrintMatrix(){
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                cout << v[i][j] << " ";
            }
            cout << endl;
        }
    }
    /*
    Matrix& operator=(const Matrix &M2){
        for(int i=0; i<m_size; i++){
            for(int j=0; j<m_size; j++){
                this->v[i][j] = M2.v[i][j];
            }
        }
        return *this;
    }
    */
};




int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N;
    long long B;
    fin >> N >> B;
    vector<vector<long long > > arr(N, vector<long long>(N,0));
    
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            fin >> arr[i][j];
        }
    }
    
    Matrix matrix(N,arr);
    matrix.pow(B).PrintMatrix();
}

