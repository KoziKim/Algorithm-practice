import sys
input = sys.stdin.readline

n = int(input())
picel = []

for i in range(n):
    picel.append(list(map(int, input().rstrip())))
    

def tree(x, y, n):
   
    
    color = picel[x][y]
    is_samecolor = True
    for i in range(x , x+ n):
        if not is_samecolor:
            break
        
        for j in range(y, y+n):
            if picel[i][j] != color:
                is_samecolor = False
                break
            
    if is_samecolor:
        if color == 0:
            print(0, end='')
        else:
            print(1, end = '')
            
    elif not is_samecolor:
        print('(', end ='')
        tree(x,y,n//2)
        tree(x,y+n//2,n//2)
        tree(x+n//2,y,n//2)
        tree(x+n//2,y+n//2,n//2)
        print(')', end ='')
        
tree(0,0,n)