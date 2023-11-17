function solution(s) {
    let answer = 0;
    let tmp = s.split(" ");
    tmp.map((_, i) => tmp[i] === "Z" ? answer -= +tmp[i-1] : answer += +tmp[i]);
    return answer;
}