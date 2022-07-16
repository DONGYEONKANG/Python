# Sequence
# 나열되어있는데, 순서가 있는...!
# Python list는 시퀸스하다.

# 컨테이너(Container : 서로 다른 자료형[list, tuple, collections.deque, ...]) / 서로다른 자료형을 담을 수 있는 것이 컨테이너 자료형이다
# Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview]

# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 리스트 및 튜플 고급!!!!!!


# 지능형 리스트(Comprehending Lists)
chars = "+_)(&*$#^&*)" # flat이자 불변
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending List 
code_list2 = [ord(s) for s in chars]

print(code_list2)

# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x : x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)


# Generator
# 시퀸스 결과를 만들어내고, 강력한 iterator(순회가 가능한 모든 객체)
# iterator같은 경우 모두 메모리에 올라가기에 대용량 처리를 하기에 비효율적이다
# 한 번에 한 개의 항목을 생성(메모리 유지x) / 무한 반복이가능하다!

import array

tuple_g = (ord(s) for s in chars)
array_g = array.array("I", (ord(s) for s in chars))

print(tuple_g) # 아직 값을 생성하지 않고, 준비하고 있는 상태
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(type(array_g))
print(array_g.tolist())

# 재네레이터 예제
print(("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)))

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print(s)


print()
print()

# 리스트 주의(얕은 복사와 깊은 복사)
marks1 = [["~"] * 3 for _ in range(4)] # 모두가 다른 주소 리스트 값
marks2 = [["~"] * 3 ] * 4 # id값이 주소만 복사가 됨

marks1[0][1] = "x"
marks2[0][1] = "x"

print(marks1)
print(marks2)

print([id(i) for i in marks1])
print([id(i) for i in marks2])