function recursiveMultiplication(a, b) {
  if (b === 0) {
    return 0;
  } else {
    return a + recursiveMultiplication(a, b - 1);
  }
}

console.log(recursiveMultiplication(4, 5));
console.log(recursiveMultiplication(3, 3));
console.log(recursiveMultiplication(0, 2));
console.log('Time Complexity: O(b)');
console.log('Space Complexity: O(b)');