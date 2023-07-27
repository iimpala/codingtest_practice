import sys

n, k = tuple(map(int, sys.stdin.readline().strip().split(" ")))

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


front = Node(1, None, None)
prev = front
for i in range(1, n):
    node = Node(i + 1, prev, None)
    prev.next = node
    prev = node

prev.next = front
front.prev = prev

result = []
node = front.prev
while node.next is not node:
    for _ in range(k):
        node = node.next
    result.append(node.value)

    node.prev.next = node.next
    node.next.prev = node.prev

if n == 1:
    result.append(1)

print(f"<{', '.join(map(str, result))}>")
