def main():
    email_stack = []
    max_stack = []
    num_tests = int(input())
    for i in range(num_tests):
        instructions = input().split()
        if instructions[0] == '1':
            email_stack.append(int(instructions[1]))
            if max_stack:
                max_stack.append(max(max_stack[-1], int(instructions[1])))
            else:
                max_stack.append(int(instructions[1]))
        elif instructions[0] == '2':
            email_stack.pop()
            max_stack.pop()
        else:
            print(max_stack[-1])

if __name__ == "__main__":
    main()