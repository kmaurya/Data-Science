# ----------------   Synchronous code -----------------------
#
# import requests
#
# from timer import timer
#
# URL = "https://httpbin.org/uuid"
#
# def fetch(session, url):
#     with session.get(url) as response:
#         print(response.json()['uuid'])
#
# @timer(1,1)
# def main():
#     with requests.Session() as session:
#         for _ in range(100):
#             fetch(session,URL)
#
#
# ------------------ Multiprocessing using poll class-----------------
#
# import requests
# from timer import timer
# from multiprocessing.pool import Pool
#
# URL = 'https://httpbin.org/uuid'
#
#
# def fetch(session, url):
#     with session.get(url) as response:
#         print(response.json()['uuid'])
#
#
# @timer(1, 1)
# def main():
#     with Pool() as pool:
#         with requests.Session() as session:
#             pool.starmap(fetch, [(session, URL) for _ in range(10)])
#
#
# ------------------------ Multithreading ThreadPoolExecutor ------------------------------
# import requests
# from concurrent.futures import ThreadPoolExecutor
# from timer import timer
#
# URL = "https://httpbin.org/uuid"
#
#
# def fetch(session, url):
#     with session.get(url) as response:
#         print(response.json()['uuid'])
#
#
# @timer(1, 1)
# def main():
#     with ThreadPoolExecutor(max_workers=10) as threadpool:
#         with requests.Session() as session:
#             threadpool.map(fetch, [session] * 100, [URL] * 100)
#             threadpool.shutdown(wait=True)

# ------------------------ Asyncio -------------

# import aiohttp
# import asyncio
# from timer import timer
#
# URL = 'https://httpbin.org/uuid'
#
#
# async def fetch(session, url):
#     async with session.get(url) as response:
#         result = await response.json()
#         print(result['uuid'])
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch(session, URL) for _ in range(100)]
#         await asyncio.gather(*tasks)
#
#
# @timer(1, 2)
# def func():
#     asyncio.run(main())
