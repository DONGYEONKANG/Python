"""

Section 1
Multithreading - Thread(5) - Prod vs Cons using Queue
Keyword - 생산자 소비자 패턴

"""
"""
Producer-Consumner Pattern
(1). 멀티스테드 디자인 패턴의 정석
(2). 서버측 프로그래밍의 핵심
(3). 주로 허리역활 중요

Python Event 객체
(1). Flag 초기값(0)
(2). Set() -> 1, Clear() -> 0, Wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태

"""

import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event):
    """ 네트워크 대기 상태라 가정(서버) """
    while not event.is_set():
        message = random.randint(1, 11)
        logging.info(f"Producer get message: {message}")
        queue.put(message)

    logging.info(f"Producer received event ")


# 소비자
def consumer(queue, event):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장장"""
    while not event.is_set or not queue.empty():
        message = queue.get()
        logging.info(f"Consumer storing message: {message}(size={queue.qsize()})")

    logging.info(f"Consumer received event")


if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # with Context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as execuctor:
        execuctor.submit(producer, pipeline, event)
        execuctor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(1)

        logging.info("Main : about to set event")

        # 프로그램 종료 시점
        event.set()