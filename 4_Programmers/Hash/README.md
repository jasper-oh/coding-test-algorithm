## 🙋‍♂️ Basic concept with python data structure

#### 1. list 자료형

자바의 배열 기능을 포함, 내부적으로 연결 리스트 자료구조를 채택하고 있어서 append(),remove() 등의 메소드 지원

```python
# list init
# 빈리스트 선언방법 1
a = []
# 빈리스트 선언방법 2
a = list()

n = 10
a = [0] * n
print(a)
# [0,0,0,0,0,0,0,0,0,0]
```

리스트의 인덱싱과 슬라이싱

인덱스 값을 입력해 리스트의 특정한 원소에 접근하는 것을 인덱싱이라고 함.

```python
a = [1,2,3,4,5]
print(a[-1]) # 5
print(a[-3]) # 3
# 값 변경
a[3] = 100

print(a[:2]) # [1,2,3]
```

리스트 컴프리헨션

리스트를 초기화 하는 방법 중 하나.

```python
array = [i for i in range(10) if i % 2 == 1]

print(array) # [1,3,5,7,9]

array1 = [i * i for i in range(1,5)]

print(array1) # [1,4,9,16,]

# 2차원 리스트 초기화
n = 3
m = 4

array = [[0] * m for _ in range(n)]
print(array) # [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

```

##### ✅ List method (keep adding)

```python
a = [1,4,3]
print("기본 리스트 : ",a)

a.append(2)
print("append : ",a) # [1,4,3,2]

a.sort()
print("오름차순 정렬 : ",a) # [1,2,3,4]

a.sort(reverse = True)
print("내림차순 정렬 : ",a) # [4,3,2,1]

a.reverse()
print("원소 뒤집기 : ",a) # [1,2,3,4]

a.insert(2,3)
print("인덱스 2에 3 추가 : ",a) # [1,2,3,3,4]

print("값이 3인 데이터의 수 : ",a.count(3)) # 2

a.remove(1)
print("값이 1인 데이터 삭제",a) # [2,3,3,4]

#측정한 값의 원소를 모두 제거하기

b = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in b if i not in remove_set] # 뭔가 sql 의 향기가..
print(result) # [1,2,4]

```

#### 2. tuple

튜플은 한번 선언된 값을 변경 불가

-> 그래프 알고리즘 구현 자주 사용
다익스트라 최단 경로 우선순위 큐를 이용 해당 알고리즘에서 우선순위 큐에 들어간 값은 변경 ❌ ( 비용 , 노드 )

```python
a = (1,2,3,4)
print(a)

a[2] = 7 # ERROR Tuple 대입 불가
```

#### 3. dictionary

key 와 value 의 쌍

{ "one" : 1 , "two" : 2 , "three" : 3}

##### ✅ dictionary method (keep adding)

```python
data = dict()
data["one"] = 1
data["two"] = 2
data["three"] = 3

key_list = data.keys()
value_list = data.values()
print(key_list) # key 데이터
print(value_list) # value 데이터

for key in key_list:
    print(data[key]) # 1,2,3
```

#### 4. set

- 중복허용 ❌
- 순서 ❌

리스트와 튜플은 순서가 있어서 인덱싱을 통해 자료형 값 얻기 가능 but 사전자료형 ( dictionary ) 과 집합 ( set ) 자료형은 순서가 없기 때문에 인덱싱으로 값을 얻을수 없다.

키 존재 ❌ 값 데이터만 가짐

👉 특정한 데이터가 이미 등장한 적이 있는지 여부 체크 할때 효과적

```python
# set init 1
data = set([1,1,2,3,4,4,5])
print(data)

# set init 2
data = {1,1,2,3,4,4,5}
print(data)

# 집합자료형 연산

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

```

##### ✅ dictionary method (keep adding)

```python
data = set([1,2,3])
print(data) # {1,2,3}

data.add(4)
print(data) # {1,2,3,4}

data.update([5,6])
print(data) # {1,2,3,4,5,6}

data.remove(3)
print(data) # {1,2,4,5,6}
```
