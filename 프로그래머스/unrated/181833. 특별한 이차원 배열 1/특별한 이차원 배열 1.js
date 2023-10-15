function solution(n) {
    const arr = Array.from(Array(n), () => Array(n).fill(0));
    arr.map((x, i) => x[i] = 1);
    return arr;
}