function solution(arr) {
    let tmp = []; 
    let cnt = -1;
    while (!(arr.every((v,i) => v === tmp[i]))){
        tmp = arr;
        arr = arr.map((x,i) => (!(x % 2) && x >= 50) ? 
                      x / 2 : 
                      ((x % 2) && x < 50) ? 
                      x * 2 + 1 : x);
        cnt++;
    }
    return cnt;
}