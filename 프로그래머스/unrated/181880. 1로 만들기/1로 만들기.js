function solution(num_list) {
    let cnt = 0;
    for (let i = 0; i < num_list.length; i++){
        let a = num_list[i];
        while (a !== 1) {
            a = a % 2 ? (a - 1) / 2 : a / 2;
            cnt += 1;
        }
    }
    return cnt;
}