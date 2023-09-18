function solution(myString, pat) {
    let cnt = 0;
    while (myString.includes(pat)) {
        let magic = [...pat].slice(1, pat.length).join('');
        magic = ' ' + magic;
        myString = myString.replace(pat, magic);
        cnt += 1;
    }
    return cnt;
}