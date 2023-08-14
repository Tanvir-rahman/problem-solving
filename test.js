function isValidParentheses(s) {
  const map = {
    '(': ')',
    '[': ']',
    '{': '}'
  }

  const stack = []

  for (let i = 0; i < s.length; i++) {
    const c = s[i]
    if (map[c]) {
      stack.push(map[c])
    } else if (c !== stack.pop()) {
      return false
    }
  }
  if (stack.length > 0) {
    return false
  } else {
    return true
  }
}

console.log('Is Valid parentheses:', isValidParentheses('(){[]}'));
console.log('Time and Space Complexity: O(n)');