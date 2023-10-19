const 열추가 = (arr, n) => {
    for (let i = 0; i < n; i++) {
        arr.map((x, i) => arr[i].push(0));
    }
}

const 행추가 = (arr, n) => {
    for (let i = 0; i < n; i++) {
        arr.push(Array(arr[0].length).fill(0));
    }
}

function solution(arr) {
    const n = arr[0].length - arr.length;
    n < 0 ? 열추가(arr, -n) : 행추가(arr, n);
    
    return arr;
}