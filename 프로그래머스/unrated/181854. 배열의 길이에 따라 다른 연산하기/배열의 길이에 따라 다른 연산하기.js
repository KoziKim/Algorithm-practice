function solution(arr, n) {
    arr.length % 2 ? arr.map((x, i) => i % 2 ? x : arr[i] += n) : arr.map((x, i) => !(i % 2) ? x : arr[i] += n);
    return arr;
}