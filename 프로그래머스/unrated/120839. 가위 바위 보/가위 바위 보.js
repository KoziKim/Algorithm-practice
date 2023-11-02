function solution(rsp) {
    // rsp = rsp.replaceAll("2", "3");
    // rsp = rsp.replaceAll("0", "1");
    // rsp = rsp.replaceAll("5", "6");
    // rsp = rsp.replaceAll("3", "0");
    // rsp = rsp.replaceAll("1", "5");
    // rsp = rsp.replaceAll("6", "2");
    // return rsp;
    let arr = {
        2: 0,
        0: 5,
        5: 2,
    }
    return [...rsp].reduce((a, b) => a + arr[b], "");
}