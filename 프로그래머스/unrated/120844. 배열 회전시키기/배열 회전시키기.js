function solution(numbers, direction) {
    direction === "right" ? numbers.unshift(...numbers.splice(-1)) : numbers.push(...numbers.splice(0, 1));
    return numbers;
}