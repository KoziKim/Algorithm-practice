function solution(order) {
    let answer = 0;
    [...order.toString()].map(x => x === "3" || x === "6" || x === "9" ? answer += 1 : "");
    return answer;
}