class BracketMatcher:
    def __init__(self, size):
        self.stack = [None] * size      # Fixed size stack
        self.size = size
        self.top = -1                   # Empty stack indicator
        self.bracket_pair = {')': '(', ']': '[', '}': '{'}

    def push(self, char):
        if self.top >= self.size - 1:   # Stack overflow check
            print("Stack Overflow! Cannot push:", char)
            return False
        self.top += 1
        self.stack[self.top] = char
        return True

    def pop(self):
        if self.top == -1:              # Stack underflow check
            print("Stack Underflow! Cannot pop.")
            return None
        char = self.stack[self.top]
        self.top -= 1
        return char

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def string_matching(self, string):
        for char in string:
            if char in "([{":
                if not self.push(char):
                    return False
            elif char in ")]}":
                if self.is_empty() or self.peek() != self.bracket_pair[char]:
                    return False
                self.pop()
        return self.is_empty()


if __name__ == "__main__":
    size = int(input("Enter stack size: "))
    matcher = BracketMatcher(size)

    input_string = input("Please enter the string you want to test: ")
    print("The string user has given is:", input_string)

    output = matcher.string_matching(input_string)

    if output:
        print("Given set is balanced")
    else:
        print("Mismatched Brackets in the input!!")
