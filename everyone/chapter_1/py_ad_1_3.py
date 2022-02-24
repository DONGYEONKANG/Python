"""
Chap 1-3
Shallow copy & Deep copy

"""
"""
객체의 복사 종류 : Copy, Shallow Copy, Deep Copy
정확한 이해 후 사용 -> 프로그래밍 개발 중요!
가변: list, set, dict / 나머지 불변
"""

# Ex1 = Copy
# Call by value, Call by Reference

a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list

print("Ex 1 >", id(a_list))
print("Ex 1 >", id(b_list))

b_list[2] = 100

print("Ex 1 >", a_list)
print("Ex 1 >", b_list)

# immutable : int, str, float, bool, unicode... 불변하는 객체들은 해당되지 얕은 복사 깊은 복사에 해당되지 않는다. 불변하기에...



# Ex2 - Shallow copy

import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)

print("Ex 2 >", id(c_list))
print("Ex 2 >", id(d_list))

d_list[1] = 100
print("Ex 2 >", c_list)
print("Ex 2 >", d_list)

d_list[3].append(1000)
d_list[4][1] = 10000

print("Ex 2 >", c_list) # 안의 리스트는 얕은 복사가 되지 않는다.
print("Ex 2 >", d_list)

# Ex3 - Deep Copy


e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)

print("Ex 3 >", id(e_list))
print("Ex 3 >", id(f_list))


f_list[3].append(1000)
f_list[4][1] = 10000

print("Ex 3 >", e_list) # 깊은 복사!
print("Ex 3 >", f_list)