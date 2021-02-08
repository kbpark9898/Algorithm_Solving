import sys
_dict={}
tree=''
total=0
while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break
    _dict.setdefault(tree, 0)
    _dict[tree]+=1
    total+=1


for name in sorted(_dict.keys()):
    print('{0} {1:0.4f}'.format(name, _dict[name]*100/total))