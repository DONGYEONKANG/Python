# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한 메서드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2 )


print(l_leng1)

# NamedTuple
# Dictionaty type(key-value), collection 하위에 있다. 

from collections import namedtuple


# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
# key: x, y, index: 0,1
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
print(pt4)

l_leng1 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt3.y) ** 2 )

print(l_leng1)


# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("point", "x, y")
Point3 = namedtuple("point", "x y")
Point4 = namedtuple("point", "x y x class", rename=True) # 기존 예약어나 중복을 rename으로 해결/ 난수로 변경


# 출력
print(Point1, Point2, Point3, Point4)


# Dict to Unpacking
temp_dict = {"x" : 75, "y" : 55}

p1 = Point1(10, 209)
p2 = Point2(x=20, y=40)
p3 = Point2(45, 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)


print()

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)


# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성 / casting
p4 = Point1._make(temp)

print(p4)

# _fields: 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict(): OrderedDict()
print(p1._asdict())
print(p4._asdict())


# 실 사용 실습
# 반20명, 4개의 반(A, B, C, D)

Classes = namedtuple("classes", ["rank", "num"])

numbers = [str(n) for n in range(1, 21)]
ranks= "A B C D".split()

print(numbers)
print(ranks)


# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))

# 추천
students2 = [Classes(rank, number)
            for rank in "A B C D".split()
                for number in [str(n)
                    for n in range(1, 21)]]


print(len(students2))