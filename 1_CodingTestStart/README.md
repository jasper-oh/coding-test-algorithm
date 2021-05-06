## Python Useful CodingTest Method

#### input output

1. 입력받은 문자열을 띄어쓰기로 구분해 정수형으로 저장

```python
list(map(int,input().split()))

```

2. 빠르게 입력 받기

```python
import sys
sys.stdin.readline().rstrip()

```

- rstrip()
  - readline() 시에 줄바꿈 기호로 입력된 공백 문자 제거

---

```python
ord()
# char -> int

print(ord('a'))
# 97

print(chr(ord('a')))
# a
```

---

```python
import random
#  0.0 <  x  < 1.0

print(random.random())

randrange(start, stop, step)
```

---

#### 자료 구조 기초

1. Stack

```python

> 상자 쌓기를 생각하면 된다.

stack = []

stack.append(5)
stack.append(2)
stack.append(1)
stack.pop()
stack.append(4)
stack.append(7)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

#[5,2,4]
#[4,2,5]

```

2. Queue

> 외부 라이브러리를 사용해야 한다. => deque
> 놀이공원 줄서기를 생각

```python

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(1)
queue.popleft()
queue.append(4)
queue.append(7)
queue.popleft()

print(queue) # 먼저 들어온 원소부터 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력

# deque([1,4,7])
# deque([7,4,1])

```
