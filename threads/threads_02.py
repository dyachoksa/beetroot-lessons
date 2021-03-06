import functools
import time
import uuid
import threading
import random
import sys


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return result

    return wrapper


def process_job(job_id):
    delay = random.randint(1, 4)
    # delay = 2

    print("Started processing job", job_id, f"[delay={delay}]")

    # Usualy we are doing network/database intensive operation here
    # ...
    time.sleep(delay)

    print("Finished processing job", job_id)


@timer
def main():
    threads_num = 5

    threads = [threading.Thread(target=process_job, args=(
        str(uuid.uuid4()),)) for _ in range(threads_num)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
    sys.exit(0)
