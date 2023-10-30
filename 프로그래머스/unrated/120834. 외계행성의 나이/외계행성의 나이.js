function solution(age) {
    let strAge = ('' + age);
    let ans = '';
    for (const i of strAge) {
        ans += String.fromCharCode(97 + +i);
    }
    return ans;
}