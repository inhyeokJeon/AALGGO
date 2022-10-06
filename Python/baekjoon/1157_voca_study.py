from collections import Counter
import sys
word = sys.stdin.readline().strip()
word = word.upper()
counter = Counter(word)
alphabet = counter.most_common(1)[0][0]
most_use_num = counter.pop(alphabet)
if counter:
    if most_use_num == counter.pop(counter.most_common(1)[0][0]):
        print("?")
    else:
        print(alphabet)
else:
    print(alphabet)