function nPush(n) {
    let tmp = [];
    for (let i = 0; i < n*2; i++){
        tmp.push(n);
    }
    return tmp;
}

function solution(arr, flag) {
    let X = [];
    arr.map((x, i) => flag[i] ? X.push(...nPush(arr[i]))
                   : X = X.slice(0, X.length - arr[i]));
    return X;
}