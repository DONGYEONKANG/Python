"""
Chap 3
Meta Class
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""

"""

메타클래스
1. 클래스를 만드는 역활 -> 의도하는 방향으로 클래스 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증 클래스 등
5. 엄격한 Class 사용 요구, 메소드 오버라이드 요구

"""

# Ex1
# type 예제

class SampleA(): # Class == Object
    pass

obj1 = SampleA() # 클래스를 인스턴스화 시켰다. , 변수에 할당, 복사 가능, 새로운 속성, 함수의 인자로 넘기기 가능하다.

# obj1 -> SampleA instance
# SampleA -> type meta class
# type -> type meta class
print("Ex1 > ", obj1.__class__)
print("Ex1 > ", type(obj1))
print("Ex1 >", obj1.__class__ is type(obj1))

print("Ex1 > ", obj1.__class__.__class__) # 모든 클래스의 메타(원형)은 type 이다.!!
print("Ex1 > ", obj1.__class__.__class__ is type(obj1).__class__) # 모든 클래스의 메타(원형)은 type 이다.!!

print(type.__class__) # 핵심 타입의 클래스도 타입이다(?)


# Ex2
# type meta(Ex1 증명)

# int, dict

n = 10
d = {"a" : 10, "b" : 20}

class SampleB():
    pass

obj2 = SampleB()

for o in (n,d,obj2):
    print(f"Ex2 > {type(o)} {type(o) is o.__class__} {o.__class__.__class__}")


print()

for t in int, float, list, tuple:
    print("Ex2 > ", type(t))

