# Sequence
# 나열되어있는데, 순서가 있는...!
# Python list는 시퀸스하다.

# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque, ...]) / 서로다른 자료형을 담을 수 있는 것이 컨테이너 자료형이다
# Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시 테이블, Dict 생성 고급 예제, Setdefault 사용법
# 해쉬테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# key에 value를 저장하는 구조

# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조 
# key 값을 해싱 함수 -> 해쉬 주소 -> Key에 대한 value 참조

# Immutable Dict 생성
# 지능형 Set
# Set 선언 최적화

# Immutable Dict

from types import MappingProxyType

d = {"key1":"value1"}

# Read Only
d_frozen = MappingProxyType(d)

# 수정 가능
d["key2"] = "value2"

# 수정 불가
# d_frozen["key2"] = "value2"

print()
print()

# set
s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set(["Apple", "Orange", "Apple", "Orange", "kiwi"])
s3 = {} #dict
s4 = set()
s5 = frozenset({"Apple", "Orange","Apple","Orange","Kiwi"})

s1.add("Melon")

print(s1)

# s5는 추가불가

# set 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행

from dis import dis

print("----------------")
print(dis("{10}"))
print("----------------")
print(dis("set([10])"))


