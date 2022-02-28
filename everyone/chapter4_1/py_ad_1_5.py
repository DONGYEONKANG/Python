"""
Chapter 1-5
Context Manager(2)

Keyword - Contextlib: Measure execution(타이머) 제작
"""

# Ex1
# Use Class
import time


class ExcuteTimer(): # with 문 안에서 실행 시간을 찾을 수 있다.
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def  __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Logging exception {(exc_type, exc_val, exc_tb)}")
        else:
            print(f"{self._msg} : {time.monotonic() - self._start} s")

        return True

with ExcuteTimer("START~!!!!!") as v:
    print(f"Recevoed start monotonic1 : {v}")
    # Excute job
    for i in range(10000000):
        pass

    raise Exception("Raise! Exception!!") # 강제로 발생


