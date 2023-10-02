function solution(arr) {
    let len = arr.length;
    let newArr = [];
    let ans = [];
    for (let i = 0; i < 100; i++) {
        if (len <= 2 ** i) {
            newArr.length = 2 ** i - len;
            newArr.fill(0);
            ans = [...arr, ...newArr];
            break;
        }
    }
    return ans;
}