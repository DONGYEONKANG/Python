# 파이썬 일급 함수(객체)
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)


# 함수 객체
def factorial(n):
    """ Factorial Function -> n : int"""
    if n == 1:
        return 1
    return n * factorial(n-1)


class A:
    pass

print(factorial(5))
print(factorial.__doc__)
print(type(factorial), type(A))
print(dir(factorial)) # 함수지만 객체 취급한다.
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)


print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))

# 함수 인수 전달 함수로 결과 반환
# map, filter, reduce

print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1, 6) if i % 2]) # 홀수만

print()
print()

# reduce 
from functools import reduce
from operator import add 

print(reduce(add, range(1,11)))
print(sum((range(1, 11))))


# 익명함수(lambda)
# 주석 필수
# 가능하면 익명함수로 리팩토링 권장

print(reduce(lambda x, t: x + t, range(1, 11)))


# Callable: 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인

print(callable(str), callable(A), callable(var_func), callable(3.14), callable(4)) # 3.14()는 호출 불가능



# partial 사용법 : 인수 고정 -> 콜백 함수 사용
# 호출만 하면 된다.
from operator import mul 
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5) # 고정되어 있다.
print(five(10))

# 고정 추가
six = partial(five, 6) 

print(five(10))
print(six())
print([five(i) for i in range(1, 11)])