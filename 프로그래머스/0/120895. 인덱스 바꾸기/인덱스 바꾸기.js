function solution(my_string, num1, num2) {
    const result = my_string.split('');
    [result[num1], result[num2]] = [my_string[num2], my_string[num1]];
    return result.join('');
}