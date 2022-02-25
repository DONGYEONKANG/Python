"""
Chap 3-3
Meta Class
Keyword - Type inheritance, Custom metaclass

"""

"""
메타클래스 상속

1. type 클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기(intercept)
    - 클래스 수정하기(modify)
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환

"""

# Ex1
# 커스텀 메타클래스 생성 예제(Type 상속X)

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

# list를 상속받음, 메소드 2개 추가

CustomList1 = type("CustomList1",
                   (list,), # 리스트를 상속받는다.
                   {
                       "desc": "커스텀 리스트1",
                       "cus_mul": cus_mul,
                       "cus_replace" : cus_replace
                   }
            )

c1 = CustomList1([1,2,3,4,5,6,7,8,9]) # self = list
c1.cus_mul(1000)
c1.cus_replace(1000, 7777)

print("Ex1 >", c1)
print("Ex1 >", c1.desc)
print("Ex1 >", dir(c1))

print()
print("-----------------------")
print()


# Ex 2
# 커스텀 메타 클래스 생성 예제(Type 상송 O)

# class MetaClassName(type): # 타입 상속
#     def __new__(metcls, name, bases, namespace):
#         코드

# new -> init -> call 순서
class CustomListMeta(type):

    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("__init__ -> ", self, object_or_name, bases, dict)

        # dict를 받아서 여기서 제어 할 수 있음(이렇게 중간에 가로채는걸 hooking 이다).
        super().__init__(object_or_name, bases, dict)

    # 안스턴스 실행
    def __call__(self, *args, **kwargs):
        print("__call__ -> ", self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print("__new__ ->", metacls, name, bases, namespace)
        namespace["desc"] = "커스텀 리스트 2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(metacls,name, bases, namespace)


CustomList2 = CustomListMeta("CustomList2", (list,), {})


c2 = CustomList2([1,2,3,4,5,6,7,8,9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print("Ex2 >", c2.desc)
print("Ex2 >", c2)


# 상속 확인(왼쪽에서 오른쪽)
print(CustomList2.__mro__)