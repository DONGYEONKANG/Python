"""

Chapter 2-1
Context Manager Annotation
Keyword - @contextlib.contextmanager, __enter__, __exit__
"""

"""
가장 대표적인 with 구문 이해
Contextlib 데코레이터 사용
코드 직관적, 예외 처리 용이성
"""
import contextlib
import time

# Ex1
# Use decorator
@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f # __enter__ 구문
    f.close() # exit

with my_file_writer("testfile4.txt", "w") as f:
    f.write("Context Manager Test4.\nContextlib Test4")


# Ex 2
# User decorator
@contextlib.contextmanager
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try: #__enter__
        yield start
    except BaseException as e:
        print(f"Loggin exception: {msg}: {e}")
        raise
    else: # __exit__
        print(f"{msg}: {time.monotonic() - start}s")


with ExcuteTimerDc("START!!!") as v:
    print(f"RECEIVED START : {v}")
    # Excute
    for i in range(30000000):
        pass
    raise ValueError("occurred.")

