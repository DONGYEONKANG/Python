"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O Bound(2) - async I/O Basic
Keyword - async I/O

"""
"""
동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU연산, DB연동, API 호출 대기 시간 늘어남 -> non-block..
파이썬 3.4 -> 비동기(asyncio) 표준 라이브러리 등장


"""
import time
import asyncio



# async def test1(): # 비동기적으로 실행된다. -> coroutine object 반환한다.
#     await test2()
#
#
#
# async def test2():
#     pass

async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n} is calculating...")
        # await time.sleep(1) # time은 async로 이루어지지 않아서 사용 불가

        await asyncio.sleep(1)

    print(f"{name} - {n} working done!")


async def process_async():
    start = time.time()

    await asyncio.wait([
        exe_calculate_async("one", 3),
        exe_calculate_async("two", 2),
        exe_calculate_async("three", 1),
    ])

    end = time.time()

    print(f">>> total seconds: {end - start}")



def exe_calculate_sync(name, n):
    for i in range(1, n+1):
        print(f"{name} -> {i} of {n} is calculating...")
        time.sleep(1)

    print(f"{name} - {n} working done!")

def process_sync():
    start = time.time()

    exe_calculate_sync("one", 3)
    exe_calculate_sync("two", 2)
    exe_calculate_sync("three", 1)

    end = time.time()

    print(f">>> total seconds: {end - start}")



if __name__ == "__main__":
    # Sync 실행
    # process_sync()

    # Async 실행
    # 파이썬 3.7
    asyncio.run(process_async())
    # asyncio.get_event_loop().run_until_complete(process_sync()) # 3.7 이하
