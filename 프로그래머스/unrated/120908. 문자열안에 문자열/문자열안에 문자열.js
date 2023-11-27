function solution(str1, str2) {
    const str3 = str1.replace(str2, ' ');
    return str1 === str3 ? 2 : 1;
}