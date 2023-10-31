function solution(emergency) {
    emergency.map((_, i) => emergency[i] += 10);
    for (let i = 0; i < emergency.length; i++){
        emergency[emergency.indexOf(Math.max(...emergency))] = i+1;
    }
    return emergency;
}