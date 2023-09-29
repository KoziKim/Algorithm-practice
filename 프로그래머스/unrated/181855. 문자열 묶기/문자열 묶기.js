function solution(strArr) {
    let len = Array(31).fill(0);
    strArr.map(x => len[x.length] += 1);
    return Math.max(...len);
}