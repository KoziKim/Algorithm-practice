function solution(myString) {
    return Array.from(myString).map(x => x <= "l" ? "l" : x).join("");
}