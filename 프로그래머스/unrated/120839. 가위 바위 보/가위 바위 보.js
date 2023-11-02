function solution(rsp) {
    rsp = rsp.replaceAll("2", "3");
    rsp = rsp.replaceAll("0", "1");
    rsp = rsp.replaceAll("5", "6");
    rsp = rsp.replaceAll("3", "0");
    rsp = rsp.replaceAll("1", "5");
    rsp = rsp.replaceAll("6", "2");
    return rsp;
}