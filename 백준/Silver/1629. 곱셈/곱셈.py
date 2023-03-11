A, B, C = map(int, input().split())

def multi_div(A, B):
    if B == 1:
        return A % C
    else:
        tmp = multi_div(A, B//2)
        if B % 2 == 0:
            return (tmp * tmp) % C
        else:
            return (tmp * tmp * A) % C
          
print(multi_div(A, B))