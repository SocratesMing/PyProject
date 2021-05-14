import asyncio
import time


# event loop
# await 只能在 async函数里面，await后面的函数定义了await关键词或者是实现了_await_函数

async def say_something(delay, words):
    print(f"Before: {words}")
    print(asyncio.get_running_loop())
    # await是一个关键字，它将执行紧跟的函数，并挂起当前协程。然后把控制交给回事件循环
    # 等后面的函数执行完后返回到当前协程继续执行
    await asyncio.sleep(delay)
    print(f"After: {words}")


async def main():
    print(f"Starting Tasks: {time.strftime('%X')}")

    task1 = asyncio.create_task(say_something(3, "First"))
    task2 = asyncio.create_task(say_something(5, "Second"))
    await task1  # 执行task1遇到await执行task2
    print("flag")
    await task2
    print(f"Finished Tasks: {time.strftime('%X')}")


asyncio.run(main())  # 运行传递进来的函数，并且管理 异步事件循环

# 1.运行异步函数main
# 2.遇到await 执行task1然后把控制交给事件循环
# 3.在task1中首先执行打印 Before: First
# 4.又遇到await 执行sleep(1)然后控制交给event loop
# 5.在task2中首先执行打印 Before: Second
# 6.此时一秒钟到了，event loop 恢复了task1的执行
# 7.task1执行完成后2秒钟到了执行恢复task2，最后执行完成task2
