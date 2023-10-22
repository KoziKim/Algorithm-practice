function solution(n) {
    return Array(n+1).fill(0).map((x, i) => i).filter(x => x % 2);
}