function solution(myStr) {
    let answer = myStr.replaceAll("a", " ").replaceAll("b", " ").replaceAll("c", " ").split(" ").filter(x => x);
    return answer.length ? answer : ["EMPTY"]
}