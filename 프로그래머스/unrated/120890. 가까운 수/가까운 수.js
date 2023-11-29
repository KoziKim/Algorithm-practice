function solution(array, n) {
    let answer = [];
    let gap = [];
    array.map(x => gap.push(Math.abs(n-x)));
    let minGap = Math.min(...gap);
    gap = gap.map(x => x-minGap);
    gap.map((x, i) => x === 0 ? answer.push(array[i]) : "");
    return Math.min(...answer);
}