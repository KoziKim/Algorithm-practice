function solution(arr, k) {
    let tmp = Array.from(new Set(arr));
    let answer = Array(k).fill(-1);
    tmp.map((x, i) => i < k ? answer[i] = x : x);
    return answer;
}