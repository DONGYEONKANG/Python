"""
Section 3
Concurrency, CPU Bound vs I/O bound - CPU Bound - Multiprocessing
Keyword - CPU Bound

"""

# CPU-Bound Multiprocessing 예제
import os
from multiprocessing import current_process, Array, Manager, Process, freeze_support
import time

# 실행 함수(계산)
def cpu_bound(number, total_list):

    """
    :param number:
    :param total_list:
    :return:
    """

    process_id = os.getpid()
    process_name = current_process().name

    # Process 정보 출력
    print(f"Process ID: {process_id}, Process name: {process_name}")

    total_list.append(sum(i * i for i in range(number))) # 공유하기 때문에 리턴이 필요없다.

def main():
    numbers = [3_000_000 + x for x in range(30)]

    # 확인
    print(numbers)

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 공유 메니저
    manager = Manager()

    # 리스트 획득(프로세스 공유)
    total_list = manager.list() # 프로세스를 공유하게 해준다.

    # 실행 시간 측정
    start_time = time.time()

    # 프로세스 생성 및 실행
    for i in numbers:
        # 생성
        t = Process(name=str(i), target=cpu_bound, args=(i, total_list,))

        # 배열에 담기
        processes.append(t)

        # 시작
        t.start()

    # Join
    for process in processes:
        process.join()

    print()

    # 결과 출력
    print(f"Total list: {total_list}")
    print(f"Sum : {sum(total_list)}")

    # 실행 시간 종료
    duration = time.time() - start_time

    print()

    # 수행 시간
    print(f"Duration: {duration} seconds")


if __name__ == "__main__":

    # 윈도우 예외시
    # freeze_support()
    main()