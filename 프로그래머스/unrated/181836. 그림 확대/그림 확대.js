function solution(picture, k) {
    let words = picture.map(x => x.split(""));
    let answer = [];
    for (const word of words) {
        let newWord = "";
        for (const w of word) {
            let newW = "";
            for (let i = 0; i < k; i++) {
                newW += w;
            }
            newWord += newW;
        }
        for (let i = 0; i < k; i++) {
            answer.push(newWord);
        }
    }
    return answer;
}