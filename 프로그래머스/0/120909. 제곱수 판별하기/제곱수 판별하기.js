function solution(n) {
    for (let i = 0; i <= n / 2; i++) {
        if (i ** 2 === n) return 1;
    }
    return 2;
}