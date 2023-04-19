while True:
    w = float(input())
    if w < 0:
        break
    print("Objects weighing ", end = '')
    print("%.2f"%w, end = '') 
    print(" on Earth will weigh ", end = '')
    print("%.2f"%(w*0.167), end = '')
    print(" on the moon.")