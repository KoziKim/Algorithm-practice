function solution(n) {
    let answer = Array.from(Array(n), () => Array(n).fill(0));
    const num = n**2;
    let tmp = n;
    let j = 0;
    let value = 1;
    if (n % 2) answer[Math.trunc(n/2)][Math.trunc(n/2)] = n**2;
    while (value < n**2) {
        for (let i = j; i < n-j; i++){
            if (answer[j][i] === 0) answer[j][i] = value;
            value++;
        }
        value--;
        for (let i = j; i < n-j; i++){
            if (answer[i][n-1-j] === 0) answer[i][n-1-j] = value;
            value++;
        }
        value--;
        for (let i = j; i < n-j; i++){
            if (answer[n-1-j][n-1-i] === 0) answer[n-1-j][n-1-i] = value;
            value++;
        }
        value--;
        for (let i = j; i < n-j; i++){
            if (answer[n-1-i][j] === 0) answer[n-1-i][j] = value;
            value++;
        }
        value--;
        j++;
    }
    return answer;
}