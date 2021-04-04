n= int(input())
rope = []
for i in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)

if n != 0:
    before_weight = rope[0]

    for i in range(1, n):
        current_rope = rope[i]
        before_weight = max(current_rope*(i+1), before_weight)

    print(before_weight)
else:
    print(0)