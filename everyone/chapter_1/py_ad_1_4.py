"""
Chapter 1-4

Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception

"""

"""
Context Manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역활을 합니다.
가장 대표적인 with 구문 이해해야한다.
정확한 이해 후 사용 프로그래밍 개발 중요하다.!

"""

# Ex1

file = open("./testfile1.txt", "w")
try:
    file.write("Context Manager Test1\nContextlib Test1")

finally:
    file.close()

# Ex2

with open("./textfile2.txt", "w") as f:
    f.write("Context Manager Test2\nContextlib Test2.")

# Ex3
# Use Class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("MyfileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print("MyFileWrited started : __exit__")

        if exc_type:
            print(f"Logging exception {(exc_type, value, trace_back)}")
        self.file_obj.close()


with MyFileWriter("./textfile3.txt", "w") as f:
    f.write("Context Manager Test3\nContextlib Test3.")


