"""

Section 1
Multithreading - Thread(3) - ThreadPoolExecutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExecutor

"""
"""

그룹 스레드(=many threads)
(1). Python 3.2 이상 표준 라이브러리 사용
(2). concurrent.futures
(3). with 사용으로 생성, 소멸 라이프사이클 관리 용이
(4). 디버깅하기가 난해함(단점)
(5). 대기중인 작업 -> 내부적으로 Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)

"""

import logging
from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    logging.info(f"Sub-Thread {name}: starting")

    res = 0
    for i in range(10001):
        res += i

    logging.info(f"Sub-Thread {name}: finishing resulting {res}")

    return res

def main():
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 실행 방법 1
    # max_workers : 작업의 개수가 넘어가면 직접 설정이 유리리
    # excutor = ThreadPoolExecutor(max_workers=3)
    # task1 = excutor.submit(task, ("First", ))
    # task2 = excutor.submit(task, ("Second",))

    # print()
    # print(task1.result())

    # 실행 방법2
    with ThreadPoolExecutor(max_workers=3) as excutor:
        tasks= excutor.map(task,["First", "Second"])

        # 결과 확인
        print(list(tasks))
if __name__ == "__main__":
    main()