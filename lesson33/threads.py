import threading
import time
import random

images = [
    "image1.jpeg",
    "image2.jpeg",
    "image3.jpeg",
    "image4.jpeg",
]


def download_image(src):
    print(f"Started loading image {src}...")
    time.sleep(random.randint(2, 5))
    # time.sleep(2)
    print(f"Finished downloading image {src}.")


def main():
    print("Image downloader.")
    start_t = time.perf_counter()

    threads = []
    for image in images:
        x = threading.Thread(target=download_image, args=(image,))
        threads.append(x)
        x.start()

    for x in threads:
        x.join()

    ent_t = time.perf_counter()

    print("All images done.")
    print("Time spent: {:.5f}".format(ent_t - start_t))


if __name__ == "__main__":
    main()
