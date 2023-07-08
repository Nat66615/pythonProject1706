import threading

counter = 0

def increment_counter():
    global counter
    counter += 1


def worker():
    for i in range(1000):
        increment_counter()


threads = []

for i in range(10):
    thread = threading.Thread(
        target=worker
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Счётчик:", counter)