import asyncio
import time

flag = True


async def sub_task():
    print(f"sub_task_start  {time.time()}")
    await asyncio.sleep(5)  # 模拟长时间的IO任务
    print(f"sub_task_stop  {time.time()}\n")


async def long_duartion():
    global flag
    await asyncio.sleep(20)
    flag = False
    pass


async def inner_loop():
    global flag
    while flag:
        print(f"in loop start {time.time()}")
        await asyncio.sleep(3)
        asyncio.create_task(sub_task())
        print(f"in loop stop {time.time()}\n")
    pass


async def test_call():
    start_time = time.time()
    await asyncio.wait(
        [asyncio.create_task(long_duartion()),  # task2
         asyncio.create_task(inner_loop())]  # task3

    )
    end_time = time.time()
    print(f"cost time  {end_time - start_time}")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(test_call())  # task1
asyncio.run(test_call())
