# 파이썬 폴더 구조 구현해보기.
# 삽입, 이동, 삭제, 복사 구현
from collections import defaultdict
import sys
from copy import deepcopy
# sys.setrecursionlimit(100000)
FILE = [
    "/",
    "/test",
    "/test/test2/test",
    "/test/test3/test4",
    "/test3",
    "/test4",
    "/test5"
]

COMMAND = [
    "add /test4/test",
    "rm /test4",
    "cp /test3 /test/test2",
    "mv /test5 /test/test3"
]

EXPECT = [
    "/test/test2/test",
    "/test/test2/test3",
    "/test/test3/test4",
    "/test/test3/test5",
    "/test3"
]

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, other):
        if other:
            next = other.pop(0)
            for child in self.children:
                if child.data == next:
                    child.add(other)
                    return
            temp = Node(next)
            temp.add(other)
            self.children.append(temp)

    def rm(self, other):
        if other:
            next = other.pop(0)
            if other:
                for child in self.children:
                    if child.data == next:
                        child.rm(other)
            else:
                index = 0
                for idx, child in enumerate(self.children):
                    if child.data == next:
                        index = idx
                        break
                self.children.pop(index)

    def search(self, other):
        if other:
            next = other.pop(0)
            for child in self.children:
                if child.data == next:
                    return child.search(other)
        else:
            return self

    def cp(self, source, dest):
        source = self.search(source)
        dest = self.search(dest)
        # print("cp", source.data, dest.data)
        dest.children.append(deepcopy(source))

    def print(self, prev):
        if not self.children:
            print(f"{prev + self.data}")
            return
        for i in self.children:
            if self.data != "/":
                i.print(prev + self.data + "/")
            else:
                i.print(prev + self.data)

    def mv(self, source_, dest_):
        source = self.search(deepcopy(source_))
        dest = self.search(dest_)
        dest.children.append(deepcopy(source))
        self.rm(source_)


def main():
    root = Node("/")
    FILE.pop(0)
    for file in FILE:
        root.add(file.split("/")[1:])

    # root.print("")
    for command in COMMAND:
        spllited = command.split()
        if spllited[0] == "add":
            root.add(spllited[1].split("/")[1:])
        elif spllited[0] == "rm":
            root.rm(spllited[1].split("/")[1:])
        elif spllited[0] == "cp":
            start = spllited[1].split("/")[1:]
            end = spllited[2].split("/")[1:]
            root.cp(start, end)
        elif spllited[0] == "mv":
            start = spllited[1].split("/")[1:]
            end = spllited[2].split("/")[1:]
            root.mv(start, end)
    root.print("")


if __name__ == "__main__":
    main()

