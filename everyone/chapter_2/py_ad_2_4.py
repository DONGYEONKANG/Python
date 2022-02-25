"""

Chapter 2-4
Method Overridng
Keyword - Overriding, OOP, 다형성
"""

"""
메서드 오버라이딩 효과
1. 서브클래스(자식)에서 슈퍼(부모)클래스를 호출 후 사용
2. 메소드 재 정의 후 사용가능
3. 부모클래스의 메소드를 추상화 후 사용가능
4. 확장 가능, 다형성(다양한 방식으로 동장)
5. 가동성 증가, 오류가능성 감소, 메소드 이름 절약
"""

class ParenteEx1():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx1(ParenteEx1):
    pass

c1 = ChildEx1()
p1 = ParenteEx1()

# 부모클래스 메소드 호출
print("Ex1 >", c1.get_value())

# c1 모든 속성 출력
print("Ex1 >", dir(c1))

# 부모 & 자식 모든 속성 출력
print("Ex1 >", dir(ParenteEx1))
print("Ex1 >", dir(ChildEx1))

print()
print("Ex1 >", ParenteEx1.__dict__)
print("Ex1 >", ChildEx1.__dict__) # namespace에 부모 클래스의 메서드가 없다. 객체를 선언할 때 메서드가 간다(?)


#Ex2
#기본 Overriding 메소드,정의

class ParentEx2():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class ChildEx2(ParentEx2):
    def get_value(self):
        return self.value * 10

c2 = ChildEx2()

# 자식 메소드 재정의 후 호출
print("Ex2 >", c2.get_value())


# Ex3
# Overriding 다형성 예제
import datetime

class Logger(object):
    def log(self, msg):
        print(msg)

class TimestampLogger(Logger):

    def log(self, msg):
        message = f"{datetime.datetime.now()} {msg}"
        super().log(message)
        # super(TimestampLogger, self).log()

class DateLogger(Logger):

    def log(self, msg):
        message = f"{datetime.datetime.now().strftime('%Y-%m-%d')} {msg}"
        # super().log(message)
        super(DateLogger, self).log(message)

l = Logger()
t = TimestampLogger()
d = DateLogger()

# 메소드 재정의 실습
print("EX3 >", l.log("Called logger .")) # print가 두번 감싸지면 None이 된다.!
print("EX3 >", t.log("Called timestamp logger."))
print("EX3 >", d.log("Called timestamp logger."))