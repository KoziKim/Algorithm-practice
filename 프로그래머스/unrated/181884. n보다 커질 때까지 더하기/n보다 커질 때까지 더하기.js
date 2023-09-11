function solution(numbers, n) {
    return numbers.reduce((a,b) => a <= n ? a+b : a, 0)
}