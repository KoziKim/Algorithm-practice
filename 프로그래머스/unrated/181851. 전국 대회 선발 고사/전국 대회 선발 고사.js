function solution(rank, attendance) {
    const [A, B, C] = rank.filter((_, i) => attendance[i]).sort((a, b) => a - b).slice(0, 3).map(x => rank.indexOf(x));
    return 10000 * A + 100 * B + C;
}