function solution(emergency) {
    // emergency.map((_, i) => emergency[i] += 10);
    // for (let i = 0; i < emergency.length; i++){
    //     emergency[emergency.indexOf(Math.max(...emergency))] = i+1;
    // }
    // return emergency;
    
    let sortedEmer = [...emergency].sort((a,b) => b - a);
    return emergency.map(x => sortedEmer.indexOf(x) + 1);
}