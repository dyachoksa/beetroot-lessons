import functools
import time
import uuid
import threading
import random


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
    # delay = random.randint(1, 4)
    delay = 2

    print("Started processing job", job_id, f"[delay={delay}]")

    # Usualy we are doing network/database intensive operation here
    # ...
    time.sleep(delay)

    print("Finished processing job", job_id)


@timer
def main():
    thread1 = threading.Thread(target=process_job, args=(str(uuid.uuid4()),))
    thread1.start()

    thread2 = threading.Thread(target=process_job, args=(str(uuid.uuid4()),))
    thread2.start()

    thread3 = threading.Thread(target=process_job, args=(str(uuid.uuid4()),))
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()


if __name__ == "__main__":
    main()
