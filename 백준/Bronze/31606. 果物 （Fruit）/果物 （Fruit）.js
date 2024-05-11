const input = (require("fs").readFileSync("dev/stdin") + '');

solution(input);
 
function solution(input){
    const [x, y] = input.split('\n');
	console.log(+x + +y + 3);
}