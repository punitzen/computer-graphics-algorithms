#include<bits/stdc++.h>
using namespace std;

void print(vector<vector<char>> mat){
    for(int i=0;i<mat.size();i++){
        for(int j=0;j<mat[0].size();j++){
            cout<<mat[i][j]<<" ";
        }
        cout<<endl;
    }
}

vector<int> dx{-1,0,1,0};
vector<int> dy{0,-1,0,1};

void flood_fill(vector<vector<char>> &mat, int i, int j,char ch, char color, int R, int C){
    if(i<0 or j<0 or i>=R or j>=C){
        return;
    }

    if(mat[i][j] != ch){
        return;
    }
    mat[i][j] = color;

    for(int k=0;k<dx.size();k++){
        flood_fill(mat,i+dx[k],j+dy[k],ch,color,R,C);
    }
}

int main(){
    vector<vector<char>> mat{
        {'.','.','.','.','.','.','.','.'},
        {'.','#','#','#','#','#','#','.'},
        {'.','#','.','.','.','.','#','.'},
        {'.','#','.','#','#','.','#','.'},
        {'.','#','.','#','#','.','#','.'},
        {'.','#','.','.','.','.','#','.'},
        {'.','#','.','.','#','#','#','.'},
        {'.','#','.','#','.','.','.','.'},
        {'.','#','.','#','.','.','.','.'},
        {'.','#','.','#','.','.','.','.'},
        {'.','#','#','#','.','.','.','.'},
        {'.','.','.','.','.','.','.','.'}
    };
    print(mat);
    // (2,2) coord to start with
    // changing color like '.' to '*' or any other char
    flood_fill(mat,2,2,'.','*',mat.size(),mat[0].size()); 
    print(mat);
    return 0;
}