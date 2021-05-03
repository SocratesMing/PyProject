
import asyncio

# async def main():
#     print('Hello ...')
#     await asyncio.sleep(1)
#     print('... World!')
#
# # Python 3.7+
# asyncio.run(main())
# print(main())

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())

