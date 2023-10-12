function solution(order) {
    return order.map(x => x.replaceAll(/(hot|ice)/g, "")).map(x => x === "cafelatte" ? 5000 : 4500).reduce((a, b) => a + b, 0);
}