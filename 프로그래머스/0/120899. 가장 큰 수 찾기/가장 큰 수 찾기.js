function solution(array) {
    let result = [];
    const maximumValue = Math.max(...array);
    array.map((x, i) => x === maximumValue ? result.push(x, i) : '')
    return result;
}