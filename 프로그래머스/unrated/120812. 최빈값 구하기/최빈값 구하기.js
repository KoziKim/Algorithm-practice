function solution(array) {
    let nums = Array(1000).fill(0);
    array.map(x => nums[x] += 1);
    let freqNum = [...nums];
    freqNum.sort((a,b) => a - b);
    if (freqNum.at(-1) === freqNum.at(-2)) return -1;
    return nums.indexOf(Math.max(...nums));
}