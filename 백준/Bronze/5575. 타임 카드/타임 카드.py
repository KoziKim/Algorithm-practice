for i in range(3):
    h, m, s, eh, em, es = map(int, input().split())
    time = eh*3600 + em*60 + es - (h*3600 + m*60 + s)
    n_h = time // 3600
    time = time % 3600
    n_m = time // 60
    n_s = time % 60
    print(n_h, n_m, n_s)