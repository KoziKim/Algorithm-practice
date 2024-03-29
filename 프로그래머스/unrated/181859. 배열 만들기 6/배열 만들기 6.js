function solution(arr) {
    let i = 0;
    let stk = [];
    while (i < arr.length) {
        if (!stk.length) {
            stk.push(arr[i]);
        } else if (stk.at(-1) === arr[i]) {
            stk.pop();
        } else if (stk.at(-1) !== arr[i]) {
            stk.push(arr[i]);
        }
        i++;
    }
    if (!stk.length) return [-1];
    return stk;
}