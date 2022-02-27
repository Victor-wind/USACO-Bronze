from collections import Counter

N= int(input())

blocks = []

block1 = input()
block2 = input()
block3 = input()
block4 = input()

'''
block1 = 'MOOOOO'
block2 = 'OOOOOO'
block3 = 'ABCDEF'
block4 = 'UVWXYZ'
'''

blocks.append(block1)
blocks.append(block2)
blocks.append(block3)
blocks.append(block4)


result = False

#print(blocks)

def search_char(s, blocks_used):
    global result
    if s == '':
        return True
    
    for i in range(4):
        if blocks_used[i] == False and s[0] in blocks[i]:
            blocks_used[i] = True
            if search_char(s[1::], blocks_used):
                return True
            blocks_used[i] = False

    return False            
    

for i in range(N):
    word = input()
    #print(word)
    blocks_used = [False, False, False, False]
    r = search_char(word, blocks_used)
    if (r) :
        print('YES')
    else:
        print('NO')
       
