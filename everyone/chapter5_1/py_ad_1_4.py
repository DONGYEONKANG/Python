"""

Section 1
Multithreading - Thread(2) - Daemon, Join
Keyword - DaemonThread, Join

"""
"""
DaemonThread(데몬스레드)
(1). 백그라운드에 실행
(2). 메인스레드 종료시 즉시 종료
(3). 주로 백그라운드 무한 대기 이벤트 발생 실행하는 부분 담당 -> JVM(가버지 컬렉션), 자동저장
(4). 일반 스레드는 작업 종료시 까지 실행


"""
import logging
import threading
import time

# 스레드는 한 번 시작하면 메인 스레드가 끝남에도 관계없이 진행된다.

# 스래드 실행 함수
def thread_func(name, d):
    logging.info(f"Sub-Thread: {name}: starting")

    for i in d:
        print(i)
    logging.info(f"Sub-Thread: {name}: finishing")


# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    # Daemon : Default False
    x = threading.Thread(target=thread_func, args=("First", range(2000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("Two", range(2000)), daemon=True)

    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # DaemonThread 확인
    print(x.isDaemon())

    # 주석 전후 결과 확인
    # 데몬스레드와 join을 같이 사용하는 것은 별로이다.
    # x.join() # 자식 스레드가 일할 동안 메인 스레드는 기다린다.
    # y.join()

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")

