//
// 파이썬으로 풀면 시간초과..
//
#include<iostream>
#include<deque>
#include<string>
#include<algorithm>
#include<functional>
using namespace std;

string front_part, back_part, koosaga, cubelover;

int main(){
    deque<char> k_deq, c_deq;
    cin>>koosaga>>cubelover;
    sort(koosaga.begin(), koosaga.end());
    sort(cubelover.begin(), cubelover.end(), greater<>());
    string solution;


    for(int i=0 ;i < (int)(koosaga.size()+1)/2; i++){
        k_deq.push_back(koosaga[i]);
    }
    for(int i=0 ;i < cubelover.size()/2; i++){
        c_deq.push_back(cubelover[i]);
    }

    for(int i=0 ;i<koosaga.size(); i++){
        if(i%2==0){
            if(c_deq.empty()||k_deq.front()< c_deq.front()){
                front_part+=k_deq.front();
                k_deq.pop_front();
            }
            else{
                back_part+=k_deq.back();
                k_deq.pop_back();
            }
        }
        else{
            if(k_deq.empty() || k_deq.front()< c_deq.front()){
                front_part+=c_deq.front();
                c_deq.pop_front();

            }
            else{
                back_part+=c_deq.back();
                c_deq.pop_back();
            }
        }
    }

    reverse(back_part.begin(), back_part.end());
    solution = front_part + back_part;
    cout<<solution;
    return 0;
}
