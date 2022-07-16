# Chapter05-02
# 일급 함수
# 클로저 기초


# 파이썬 변수 범위(scope)
# 지역 변수, 전역 변수

# Ex3

c = 30

def func_v3(a):
    print(a)
    print(c)
    c = 40 # 중복된 변수이름이면 지역변수부터
    

# Closure(클로저) 함수
# 지역함수의 변수값을 함수가 끝나고 기억한다.
# 서버 프로그래밍 -> 동시정(Concurrency) 제어 -> 같은 메모리 공간에 여러 자원이 접근 -> 교착상태(Dead Lock) 
# 메모리를 공유하지 않고 메세지 전달로 처리하기 위한 역활
# 진행도를 기억한다. / 클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
# 클로저는 불변자료구조 및 원자성, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

# **************클로저는 불변 상태를 기억한다****************

a = 100
print(a + 100)
print(a + 1000)

# 결과 누적 (함수)
print(sum(range(1, 51)))
print(sum(range(51, 101)))

# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []
        
    def __call__(self, v):
        self._series.append(v)
        print( " inner >> {} / {}".format(self._series, len(self._series)))
        
        return sum(self._series) / len(self._series)

# 인스턴스 생성
averager_cls = Averager()

# 누적 / 클래스를 이용한 예제
# 상태를 기억한다.! 
print(averager_cls(10)) # 클래스를 함수처럼~~
print(averager_cls(30))
print(averager_cls(50))
print(averager_cls(70))