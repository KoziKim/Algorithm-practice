function solution(hp) {
    let gAnt = Math.trunc(hp / 5);
    let sAnt = Math.trunc((hp - (gAnt * 5)) / 3);
    let wAnt = hp - gAnt * 5 - sAnt * 3;
    return gAnt + sAnt + wAnt;
}