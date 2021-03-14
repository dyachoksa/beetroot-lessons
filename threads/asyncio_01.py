import time
import asyncio
import threading
import os


async def count():
    print("Start of count()")
    print("Thread id:", threading.get_native_id(), "Process id:", os.getpid())

    # time.sleep(1)

    await asyncio.sleep(1)

    print("Middle of count()")

    await asyncio.sleep(1)

    print("End of count()")


async def main():
    await asyncio.gather(count(), count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()

    asyncio.run(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
