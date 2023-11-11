function solution(n) {
    let cnt = 0;
    for (let i = 3; i <= n; i++){
        for (let j = 2; j < i; j++){
            if (i % j !== 0) continue;
            cnt+=1;
            break;
        }
    }
    return cnt;
}