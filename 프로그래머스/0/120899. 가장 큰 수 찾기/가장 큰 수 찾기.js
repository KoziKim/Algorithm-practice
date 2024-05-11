function solution(array) {
    const maxValue = Math.max(...array);
    const index = array.indexOf(maxValue);
    return [maxValue, index];
}