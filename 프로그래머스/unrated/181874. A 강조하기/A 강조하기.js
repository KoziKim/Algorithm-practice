function solution(myString) {
    return [...myString].map((x,i) => x === "a" ? x.toUpperCase() : x === "A" ? x : x.toLowerCase()).join('');
}