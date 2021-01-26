#include<iostream>
#include<cmath>
using namespace std;
int queen_count=0;

bool promising(int i, int col[]){
    int k=0;
    bool check = true;
    while(k<i && check==true){
        if(col[i] == col[k] || abs(col[i]-col[k]) == i-k){
            check = false;
        }
        k+=1;
    }
    return check;
}

void queens(int n, int i, int col[]){
    if(promising(i, col)){
        if(i==n-1){
            queen_count+=1;
        }
        else{
            for(int k=0; k<=n; k++){
                col[i+1]=k;
                queens(n, i+1, col);
            }
        }
    }
}

int main(){
    int n;
    cin>>n;
    int *col = new int[n];
    for(int i=0; i<n; i++){
        col[i]=0;
    }
    queens(n, -1, col);
    cout<<queen_count;

    
}


// queen_count=0
// def promising(i,col):
//     k = 0
//     switch = True
//     while k<i and switch==True:
//         if(col[i] == col[k] or abs(col[i]-col[k]) == i-k):
//             switch = False
//         k+=1
//     return switch

// def queens(n,i,col):
//     global queen_count
//     if promising(i,col):
//         if i == n-1:
//             queen_count+=1
//         else:
//             for k in range(n):
//                 col[i+1] = k
//                 queens(n,i+1,col)

// n=int(input())
// col=n*[0]
// queens(n,-1,col)
// print(queen_count)
