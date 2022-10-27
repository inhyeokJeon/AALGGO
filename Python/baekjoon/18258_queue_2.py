import sys
from collections import deque

class Queue:
    q = deque()
    def push(self, X):
        self.q.append(X)

    def pop(self):
        if self.q:
            return self.q.popleft()
        return -1

    def size(self):
        return len(self.q)

    def empty(self):
        if self.q:
            return 0
        return 1

    def front(self):
        if self.q:
            return self.q[0]
        return -1

    def back(self):
        if self.q:
            return self.q[-1]
        return -1

K = int(sys.stdin.readline().strip())
Q = Queue()
for i in range(K):
    orders = sys.stdin.readline().strip().split()
    if len(orders) > 1:
        Q.push(int(orders[1]))
    else:
        if orders[0] == "back":
            print(Q.back())
        elif orders[0] == "front":
            print(Q.front())
        elif orders[0] == "pop":
            print(Q.pop())
        elif orders[0] == "size":
            print(Q.size())
        else:
            print(Q.empty())