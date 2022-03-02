"""
Section 3
Concurrency, CPU Bound vs I/O bound - I/O Bound(2) - Threading vs Multiprocessing vs AsyncIO
Keyword - I/O Bound, asyncio

"""
import aiohttp
import time
import asyncio

# I/O bound Asyncio 예제
# threading 보다 높은 코드 복잡도 - Async, Await 적절하게 코딩





# 실행함수1(다운로드)
async def request_site(session, url): # 전역변수 사용?

    # 세션 확인
    # print(session)
    print(session.headers)

    async with session.get(url) as response:
        print(f"Read Contents {response.content_length}, from {url}")


# 실행함수2(요청)
async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        # 작업 목록
        tasks = []
        for url in urls:
            # 태스크 목록 생성
            task = asyncio.ensure_future(request_site(session, url))
            tasks.append(task)

        # 태스크 확인
        # print(*tasks)
        # print(tasks)
        await asyncio.gather(*tasks, return_exceptions=True)



def main():
    # 테스트 URLS
    urls = [
        "https://www.jython.org",
        "http://olympus.realpython.org/login",
        "https://realpython.com"
    ] * 3

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    # 파이썬 3.7
    # asyncio.run(request_all_sites(urls)) # 시작되는 지점에는 Async 안붙여도 된다.
    asyncio.get_event_loop().run_until_complete(request_all_sites(urls)) # 3.7 이하, 지금 3.8 이상에 버그가 있다..

    # 실행
    duration = time.time() - start_time

    print()

    # 결과 출력
    print(f"Downloaded {len(urls)} sites in {duration} seconds")


if __name__ == "__main__":
    main()
