import asyncio


async def long_time_taking_method():
    await asyncio.sleep(4000)
    print("Completed the work")


async def main():
    try:
        ##关键函数wait_for和参数timeout
        await asyncio.wait_for(long_time_taking_method(), timeout=2)
    except asyncio.TimeoutError:
        print("Timeout occurred")


asyncio.run(main())
