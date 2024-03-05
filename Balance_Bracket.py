def areBracketsBalanced(expr):
	stack = []

	for char in expr:
		if char in ["(", "{", "["]:
			stack.append(char)
		else:
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			elif current_char == '{':
				if char != "}":
					return False
			elif current_char == '[':
				if char != "]":
					return False

	if stack:
		return False
	
	return True

def main():
	n = int(input("Enter the number of test cases: "))
	test_cases = [input() for _ in range(n)]

	for test_case in test_cases:
		result = areBracketsBalanced(test_case)
		print(result)

if __name__ == "__main__":
	main()
