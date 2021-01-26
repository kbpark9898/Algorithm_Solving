

queen_count=0
def promising(i,col):
    k = 0
    switch = True
    while k<i and switch==True:
        if(col[i] == col[k] or abs(col[i]-col[k]) == i-k):
            switch = False
        k+=1
    return switch

def queens(n,i,col):
    global queen_count
    if promising(i,col):
        if i == n-1:
            queen_count+=1
        else:
            for k in range(n):
                col[i+1] = k
                queens(n,i+1,col)

n=int(input())
col=n*[0]
queens(n,-1,col)
print(queen_count)
