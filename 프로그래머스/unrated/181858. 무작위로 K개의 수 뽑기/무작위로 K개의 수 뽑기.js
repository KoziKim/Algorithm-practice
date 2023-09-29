function solution(arr, k) {
    let set1 = new Set(arr);
    let tmp = Array.from(set1);
    let answer = new Array();
    answer.length = k;
    answer.fill(-1);
    tmp.map((x, i) => i < k ? answer[i] = x : x);
    return answer;   
}