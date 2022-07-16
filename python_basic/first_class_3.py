# Chapter05-03
# 일급 함수
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능


# CLosuer 사용

def closure_ex1():
    # Free val(자유변수)
    # 클로저 영역
    series = []
    
    def averager(v):
        series.append(v)    
        print("inner >>> {} / {}".format(series, len(series)))
        return sum(series) / len(series)
    
    return averager


avg_closure1 = closure_ex1()

print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))

print()
print()


# function inspection
print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print(avg_closure1.__closure__[0].cell_contents)


print()
print()

# 잘못된 클로저 사용 예시
def closure_ex2():
    # Free varialbe
    cnt = 0
    total = 0
    
    def averager(v):
        cnt += 1
        total += v
        return total / cnt
    
    return averager


avg_closure2 = closure_ex2()
# print(avg_closure2(10)) 예외


# 수정
def closure_ex3():
    # Free varialbe
    cnt = 0
    total = 0
    
    def averager(v):
        nonlocal cnt, total  # nonlocal를 활용해 자유 변수로~!
        cnt += 1
        total += v
        return total / cnt
    
    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))