function solution(n_str) {
    let arrN = Array.from(n_str);
    while (arrN[0] === "0") {
        arrN = arrN.splice(1);
    }
    return arrN.join("");
}