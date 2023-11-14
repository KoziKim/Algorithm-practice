function solution(my_string) {
    let num = [...my_string.replace(/[a-zA-Z]/g, '')].sort((a, b) => a - b);
    num.map((x, i) => num[i] = +num[i]);
    return num;
}