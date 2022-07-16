# Sequence
# 나열되어있는데, 순서가 있는...!
# Python list는 시퀸스하다.

# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque, ...]) / 서로다른 자료형을 담을 수 있는 것이 컨테이너 자료형이다
# Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시 테이블, Dict 생성 고급 예제, Setdefault 사용법
# key에 value를 저장하는 구조

# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조 
# key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 value 참조

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인 / 불변형만 hash 값을 확인할 수 있다.

t1 = (10, 20 ,(30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))
# print(hash(t2))

print()
print()

# Dict Setdefult 예제
source = (("k1", "val1"),
        ("k1", "val2"),
        ("k2", "val3"),
        ("k2", "val4"),
        ("k2", "val5"))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
        
    else:
        new_dict1[k] = [v]
        
print(new_dict1)
    

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
    
print(new_dict2)


