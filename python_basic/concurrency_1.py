# Chapter 06-01
# 병행성(Concurrency)

# iterator and generators
# 제네레이터는 반복 가능한 객체를 생상한다.
# iterable이란 반복 가능한 객체이다.

# 파이썬 반복 가능한 타입
# collections, text file, List, Dict, Set, Tuple, unpacking : iterable

# 반복 가능한 이유? -> 내부적으로 iter(x) 함수 호출
t = "ABCDEFGHIJKLMNOPQRSTQVWCX"

print(dir(t))

for c in t:
    print(c)
    
    
# while
w = iter(t)

while True:
    try:
        print(next(w))
        
    except StopIteration:
        break
    
print()


# 반복형 확인
from collections import abc

print(hasattr(t, "__iter__"))
print(isinstance(t, abc.Iterable))

print()
print()


# next 패턴
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")
        
    def __next__(self):
        # print("Called __next__")
        try:
            word = self._text[self._idx]
            
        except IndexError:
            raise StopIteration("Stopped Iteration")
        
        self._idx += 1
        
        return word
    
    def __repr__(self):
        return "WordSplit(%s)" % (self._text)
    
    
wd = WordSplitter("Do today what you could do tommorrow")

print(wd)
print(next(wd))
print(next(wd))
print(next(wd))
print(next(wd))
print(next(wd))
print(next(wd))
print(next(wd))


# Generator 패턴
# 1. 지능형 리스트, 딕셧너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2. 단위 실행 가능한 코루틴()
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ")
        
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
            
        return
    
    def __repr__(self):
        return "WordSplitGenerator(%s)" % (self._text)
    
wg = WordSplitGenerator("Do today what you could do tommorrow")

wt = iter(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
