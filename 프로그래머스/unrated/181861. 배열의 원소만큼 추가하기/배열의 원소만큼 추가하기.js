function pushBack(el) {
    let X = [];
    for (let i = 0; i < el; i++){
        X.push(el);
    }
    return X;
}

function solution(arr) {
    let ans = [];
    arr.map(x => ans.push(...pushBack(x)));
    return ans;
}