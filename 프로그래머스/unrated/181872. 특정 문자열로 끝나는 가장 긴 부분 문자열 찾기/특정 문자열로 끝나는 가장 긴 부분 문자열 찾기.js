function solution(myString, pat) {
    let lastIdx = myString.lastIndexOf(pat);
    return myString.slice(0, lastIdx + pat.length);
}