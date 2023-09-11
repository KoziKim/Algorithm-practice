function solution(numbers, n) {
    let answer = numbers.reduce((a,b) => a <= n ? a+b : a, 0) 
    return answer;
}