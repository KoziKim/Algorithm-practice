function solution(my_string) {
    let answer = '';
    [...my_string].map((x, i) => 65 <= my_string.charCodeAt(i) && my_string.charCodeAt(i) <= 90 ? answer += String.fromCharCode(my_string.charCodeAt(i) + 32) : answer += String.fromCharCode(my_string.charCodeAt(i) - 32 ));
    return answer;
}