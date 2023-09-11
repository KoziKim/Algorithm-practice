function solution(arr, queries) {
    for (let i = 0; i < queries.length; i++) {
        let [a, b] = queries[i];
        for (let j = a; j < b+1; j++) {
            arr[j] += 1;
        }
    }
    return arr;
}