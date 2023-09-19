function solution(strArr) {
    return strArr.map(x => x.includes("ad") ? null : x).filter(x => x);
}