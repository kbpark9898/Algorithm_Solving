import sys 
sys.setrecursionlimit(10**6)
k = int(input())
inorder=list(map(int, input().split()))
postorder = list(map(int, input().split()))

inodrder_index = [0 for i in range(k+1)]

for i in range(len(inorder)):
    inodrder_index[inorder[i]] = i

def getPreOrder(in_start, in_end, post_start, post_end):
    if in_start>in_end or post_start>post_end:
        return
    root = postorder[post_end]
    in_root = inodrder_index[root]
    print(root, end=" ")
    post_left_length = in_root - in_start 
    getPreOrder(in_start, in_root-1, post_start, post_start+post_left_length-1 )
    getPreOrder(in_root+1, in_end, post_start+post_left_length, post_end-1)

getPreOrder(0, k-1, 0, k-1)


