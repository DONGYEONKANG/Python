"""
Section 2
Parallelism with Multiprocessing - Queue, pipe
keyword - Queue, Pipe, Communications between processes

"""

# 프로세스 통신 구현 Queue
from multiprocessing import Process, Queue, current_process
import time
import os


def worker(id, baseNUm, q):
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(baseNUm):
        sub_total += i

    # Produce
    q.put(sub_total)

    # 정보 출력
    print(f"Process ID: {process_id},Process Name : {process_name}, ID: {id}")
    print(f"Result : {sub_total}")


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()

    # 출력
    print(f"Parent process ID {parent_process_id}")

    # 프로세스 리스트 선언
    processes = list()

    # 시작시간
    start_time = time.time()

    # Queue 선언
    q = Queue()
    for i in range(5): # 1 ~100
        # 생성
        t = Process(name=str(i), target= worker, args=(i, 10000000, q))

        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()
    # Join
    for process in processes:
        process.join()

    # 순수 계산 시간
    print(f"---{time.time() - start_time} seconds---")

    # 종료 플레크
    q.put("exit")

    # 대기
    total = 0
    while True:
        tmp = q.get()
        if tmp == "exit":
            break
        else:
            total += tmp
    print()

    print(f"Main-Processing Total count={total}")


if __name__ == "__main__":
    main()