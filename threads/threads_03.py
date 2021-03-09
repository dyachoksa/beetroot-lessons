import functools
import time
import uuid
import threading
import random
import sys
import concurrent.futures


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

    print("Started processing job", job_id,
          f"[delay={delay}, thread_id={threading.get_native_id()}]")

    # Usualy we are doing network/database intensive operation here
    # ...
    time.sleep(delay)

    print("Finished processing job", job_id)


@timer
def main():
    threads_num = 5

    jobs = [str(uuid.uuid4()) for _ in range(10)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads_num) as executor:
        executor.map(process_job, jobs)


if __name__ == "__main__":
    main()
    sys.exit(0)
