function factorial(x) {
    if (x === 0) return 1;
    if (x === 1) return 1;
    return x*factorial(x-1);
}

function solution(balls, share) {
    let nFact = factorial(balls)
    let nMFact = factorial(balls-share)
    let mFact = factorial(share);
    return Math.round(nFact / (nMFact * mFact));
}