
"""
Chapter 2-2
Property - Underscore
Keyword - access modifier(접근지정자), underscore

"""
"""
다양한 언더스코어 활용
파이썬 접근지정자 설명
"""
# Ex1
# Use underscore
# 1. 인터프리터, 2. 값 무시, 3.네이밍(국제화, 자릿수)

# Unpacking
x, _, y = (1, 2, 3)
print(x, y)
a, *_, b = (1, 2, 3, 4, 5)
print(a,b)

for _ in range(10):
    pass

for _, val in enumerate(range(10)):
    pass


# Ex2
# 접근지정자
# name : public
# _name : protected
# __name : private
# 파이썬 -> Public 강제X, 약속된 규약에 따라 코딩 장려(자유도, 책임감 장려)
# 타 클래스(클래스 변수, 인스턴스 변수 값 쓰기 장려 안함) -> Naming Mangling
# 타 클래스 __ 접근하지 않는 것이 원칙

# No use Property

class SampleA:
    def __init__(self):
        self.x = 0
        self.__y = 0
        self._z = 0

a = SampleA()
a.x = 1
print(f"EX2 > x : {a.x}")
# print(f"EX2 > y : {a.__y}")
print(f"EX2 > z : {a._z}")
print(f"EX2 > : {dir(a)}")

a.__SampleA__y = 3 # 수정 가능
print(f"EX2 > : {a.__SampleA__y}")

class SampleB:
    def __init__(self):
        self.x = 0
        self.__y = 0 # __SampleB__ya.__SampleA__y

    def get_y(self):
        return self.__y

    def set_y(self, value):
        self.__y = value

b = SampleB()
b.x = 1
b.set_y(2)

print(b.get_y())
