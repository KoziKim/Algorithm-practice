function solution(myStr) {
    let answer = myStr.split(/[abc]/).filter(x => x);
    return answer.length ? answer : ["EMPTY"]
}