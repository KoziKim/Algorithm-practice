const fs = require("fs");
const rawInput = fs.readFileSync("dev/stdin").toString().trim().split("\n");
 
const input = rawInput[0].split(' ');

solution(input);
 
function solution(input){
    const num = (n) => input[n]

    const answer = num(0) * num(1) - num(2) * num(3) * num(4);

	console.log(answer);
}