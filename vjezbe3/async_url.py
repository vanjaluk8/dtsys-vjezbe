# url async sending requests using asyncio and aiohttp. Write a Python program that sends async http requets to some urls.
import asyncio
import aiohttp

# write an async function that sends a GET request towards a defined url using aiohttp. The funciton should take the reply and write the lenght of the reply. Put also async.sleep(x) to simulate a delay of x seconds
async def get_url(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f'URL: {url} - {len(await response.text())} bytes - {response.status}')
                await asyncio.sleep(5)
                print(f'URL: {url} - {len(await response.text())} bytes after sleep - {response.status}')
    except aiohttp.ClientError as e:
        print(f'URL: {url} - {e}')
        
# main async funcition. Define a main async functuon main(). Inside write a list of URL that should be used for the requests. 
async def main():
    urls = [
        'https://google.hr',
        'https://python.org',
        'https://github.com',
        'https://stackoverflow.com',
        'https://ww.youtube.com'
    ]
# create async tasks. in the main function crate lists of async tasks using asyncio.create_task(). every task should call the get_url() function with a different url from the list
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url(url))) # create a task for every url in the list
    await asyncio.gather(*tasks) # gather all the tasks in a single list and execute them


# executing the tasks. using await asyncio.gather() execute the tasks
if __name__ == "__main__":
    while True:
        asyncio.run(main())
