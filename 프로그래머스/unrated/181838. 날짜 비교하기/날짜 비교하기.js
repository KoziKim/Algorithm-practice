function solution(date1, date2) {
    // let [a, b, c, d, e, f] = [...date1, ...date2];
    // [a, b, c, d, e, f] = [+a, +b, +c, +d, +e, +f];
    // if (a < d) return 1;
    // if (a === d){
    //     if (b < e) return 1;
    //     if (b === e && c < f) return 1;   
    // }
    // return 0;
    
    return new Date(date1) < new Date(date2) ? 1 : 0;
}