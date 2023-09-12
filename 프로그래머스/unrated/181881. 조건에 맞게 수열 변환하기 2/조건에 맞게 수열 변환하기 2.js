function solution(arr) {
    let tmp; 
    let cnt = 0;
    while (true){
        tmp = arr;
        arr = arr.map((x,i) => (!(x % 2) && x >= 50) ? x / 2 : 
                      ((x % 2) && x < 50) ? x * 2 + 1 : x);
        if (arr.every((v,i) => v === tmp[i])) return cnt;
        cnt++;
    }
}