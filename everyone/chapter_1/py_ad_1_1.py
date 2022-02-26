"""

chap 1-1
Variable Scope

Keyword - scope, global, nonlocal, locals, globals....
"""

"""
전역변수는 주로 변하지 않는 고정 값에 사용 (상수)
지역변수 사용 이유: 지역변수는 함수 내에 로직 해결에 국한, 소멸주기: 함수 실행 해제 시
전역변수를 지역내에서 수정되는 것은 권장X global(?)

"""

# Ex1
a = 10 # Global variable

def foo():
    # Read global variable
    print("EX 1 >", a)

# Ex 2
b = 20

def bar():
    b = 30
    print("EX 2 >", b)


# Ex 3
c = 40

def foobar():
    # c = c + 10
    print("EX 3 >", c) # UnboundLocalError 참조 에러!!


# Ex 4
d = 40

def barfoo():
    # c = c + 10
    global d
    d = 60
    d += 100
    print("EX 4 >", d)


# Ex 5(중요) nonlocal
def outer(): # Closure
    e = 70
    def inner(): # 지역 변수 안에 지역변수를 수정할 떄
        nonlocal e
        e += 10
        print("EX 5 >", e)
    return inner

# EX 6

def func(var):
    x = 10
    def printer():
        print( "Ex 6 >", "print Func Inner" )

    print("Func Inner", locals()) # 함수안의 지역변수들을 호출한다 !@!!



if __name__ == "__main__":
    # Ex 1
    foo()

    # EX 2
    bar()

    # EX 3
    foobar() # UnboundLocalError 참조 에러!!

    # Ex 4
    barfoo()

    # Ex 5
    in_test = outer() # Closure
    in_test()
    in_test()

    # Ex 6
    func("Hi")

    # Ex 7
    print("EX7 >", globals())

    globals()["test_varable"] = 10 # 실제로는 이렇게 실행된다.!!

    print("EX7 >", globals())

    # Ex 8 (지역 -> 전역 변수 생성)
    for i in range(1, 10):
        for k in range(1,10):
            globals()[f"plus_{i}_{k}"] = i + k # 동적으로 생성한다.

    print(globals())
