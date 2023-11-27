function solution(array, n) {
    let answer = 0;
    array.map(x => x === n ? answer += 1 : '');
    return answer;
}