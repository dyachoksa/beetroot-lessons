import functools
import time
import uuid
import random
import sys
import multiprocessing


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
    res = 0
    for x in range(100_000_000):
        res = res + (x*2 - x) / 3

    print("Finished processing job", job_id)


@timer
def main():
    processes_num = 5

    jobs = [str(uuid.uuid4()) for _ in range(5)]

    with multiprocessing.Pool(processes=processes_num) as executor:
        executor.map(process_job, jobs)


if __name__ == "__main__":
    main()
    sys.exit(0)
