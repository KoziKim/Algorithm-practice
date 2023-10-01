function solution(arr1, arr2) {
    let ans = arr1.length > arr2.length ? 1 : arr1.length < arr2.length ? -1 : 0;
    if (arr1.length === arr2.length) {
        arr1Sum = arr1.reduce((a, b) => a + b, 0);
        arr2Sum = arr2.reduce((a, b) => a + b, 0);
        ans = arr1Sum > arr2Sum ? 1 : arr1Sum < arr2Sum ? -1 : 0;
    }
    return ans;
}