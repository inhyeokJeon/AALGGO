import sys

class Stack:
    stack = []
    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        return 1

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1


K = int(sys.stdin.readline().strip())
stack = Stack()
for i in range(K):
    orders = sys.stdin.readline().strip().split()
    if len(orders) > 1:
        stack.push(int(orders[1]))
    else:
        if orders[0] == "top":
            print(stack.top())
        elif orders[0] == "pop":
            print(stack.pop())
        elif orders[0] == "size":
            print(stack.size())
        else:
            print(stack.empty())