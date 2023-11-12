function solution(my_string) {
    const regex = new RegExp(/[^aeiou]/);
    return [...my_string].filter(x => regex.test(x)).join('');
}