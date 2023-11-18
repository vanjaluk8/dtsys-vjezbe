# ASYNC API JSON RETRIEVEAL (PARALLEL REQUESTS)
# write a program that uses asyncio and aiohttp for fetching data from a REST API. execute HTTP GET requests towards multiple urls, in the same time grab JSON data and print some JSON parts from every API response
# 1. use the following urls:
# https://jsonplaceholder.typicode.com/posts/1
# https://jsonplaceholder.typicode.com/posts/2
# https://jsonplaceholder.typicode.com/posts/3

# 2. grab json data from every api response
# 3. for every response print the following data:
# userId (korisnički identifikator)
# id (identifikator)
# title (naslov)
# body (sadržaj)

# Use aysnc/await syntax and aiohttp library for sending requests and grabbing responses
# Use asyncio.gather() for executing multiple requests in the same time
# Use asyncio.run() for executing the main async function


import asyncio
import aiohttp

def print_json(json):
    print(f'userId: {json["userId"]}')
    print(f'id: {json["id"]}')
    print(f'title: {json["title"]}')
    print(f'body: {json["body"]}')
    print('------------------------')

async def get_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                json = await response.json()
                print_json(json)
    except aiohttp.ClientError as e:
        print(f'URL: {url} - {e}')

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2',
        'https://jsonplaceholder.typicode.com/posts/3'
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url(url)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    while True:
        asyncio.run(main())
    