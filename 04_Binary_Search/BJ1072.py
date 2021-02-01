total, win = map(int, input().split())
current_win_rate = (win*100)//total
def win_rate(total_game, win_game):
    return (win_game*100)//total_game

def p_search():
    left=0
    right = 1000000000
    while left<=right:
        mid=(left+right)//2
        if win_rate(total+mid, win+mid)==current_win_rate:
            left=mid+1
        else:
            right=mid-1
    if win_rate(total+left, win+left)==current_win_rate:
        return -1
    else:
        return left
print(p_search())
