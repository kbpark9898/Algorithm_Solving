class Node:
    def __init__(self, current, left, right):
        self.current = current
        self.left = left
        self.right = right
    

def preorder(tree, node):
    print(node.current, end='')
    if node.left !='.':
        preorder(tree, tree[node.left])
    if node.right !='.':
        preorder(tree, tree[node.right])


def inorder(tree, node):
    if node.left!='.':
        inorder(tree, tree[node.left])
    print(node.current, end='')
    if node.right!='.':
        inorder(tree, tree[node.right])

def postorder(tree, node):
    if node.left!='.':
        postorder(tree, tree[node.left])
    if node.right!='.':
        postorder(tree, tree[node.right])
    print(node.current, end='')


k=int(input())
tree={}
for i in range(k):
    parent, left, right = map(str, input().split())
    
    tree[parent] = Node(current=parent, left=left, right=right)


preorder(tree, tree['A'])
print()
inorder(tree, tree['A'])
print()
postorder(tree, tree['A'])

