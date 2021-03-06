"""
Section 2
Parallelism with Multiprocessing - Sharing state
keyword - memory sharingm array, value
"""

from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제(공유 O)

# 실행함수
def generate_update_numver(v: int):
    for _ in range(50):
        v.value += 1
    print(current_process().name, "data", v.value)

def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()

    # 출력
    print(f"Parent process ID {parent_process_id}")

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 메로리 공유 변수
    # from multiprocess import shared_memory 사용 가능(파이썬 3.8)
    # from multiprocess import Manager 사용 가능
    # share_numbers = Array("i", range(50))
    share_value = Value("i", 0) # "i" int, "f" float, "c" char...

    for _ in range(1,10):
        # 생성
        p = Process(target=generate_update_numver, args=(share_value,))

        # 배열에 담기
        processes.append(p)

        # 실행
        p.start()

    # join
    for p in processes:
        p.join()

    # 최족 프로세스 부모 변수 확인
    print("Final Data in parent process", share_value)


if __name__ == "__main__":
    main()