# Special(Magic) Method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한 메서드

# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 풀력
print(dir(int))
print(dir(float))

n = 10

print(n + 100)
print(n.__add__(100))
print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))
