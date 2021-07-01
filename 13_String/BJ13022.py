word = input()


h={'w':0,'o':0,'l':0,'f':0 }


is_break = False
if word[0] == 'w':
    h['w']+=1
    for i in range(1, len(word)):
        if word[i] =='w':
            if h['o'] == h['l'] == h['f']:
                if h['o'] == h['l'] == h['f']==0:
                    h['w'] +=1
                else:
                    h={'w':1,'o':0,'l':0,'f':0 }
            else:
                print(0)
                is_break = True
                break

        elif word[i] == 'o':
            if h['w'] == 0:
                print(0)
                is_break = True
                break
            else:
                h['o']+=1
                if h['w'] < h['o']:
                    print(0)
                    is_break = True
                    break
        elif word[i] == 'l':
            if h['w'] != h['o']:
                print(0)
                is_break = True
                break
            if 0 in (h['w'], h['o']):
                print(0)
                is_break = True
                break
            else:
                h['l']+=1
                if h['o'] < h['l']:
                    print(0)
                    is_break = True
                    break

        elif word[i] == 'f':
            if not(h['w'] == h['o'] == h['l']):
                print(0)
                is_break = True
                break
            if 0 in (h['w'], h['o'],h['l']):
                print(0)
                is_break = True
                break
            else:
                h['f']+=1
                if h['l'] < h['f']:
                    print(0)
                    is_break = True
                    break
    if not is_break:
        if h['w'] == h['o'] == h['l'] == h['f']:
            print(1)
        else:
            print(0)

else:
    print(0)