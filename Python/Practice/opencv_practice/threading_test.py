import threading
import time


st = time.time()


def job():
    for i in range(5):
        print("Child thread: ", i)
        time.sleep(5)


t = threading.Thread(target=job)
t.start()

for i in range(3):
    print("Main thread: ", i)
    time.sleep(1)

t.join()
end = time.time()
print("spend time: ", end - st)
