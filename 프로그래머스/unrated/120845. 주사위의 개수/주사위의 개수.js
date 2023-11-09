function solution(box, n) {
    const x = Math.trunc(box[0] / n);
    const y = Math.trunc(box[1] / n);
    const z = Math.trunc(box[2] / n);
    return x * y * z;
}