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












