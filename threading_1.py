import threading

def count_num():
    for i in range(1,6):

        print(f"here is numbers: {i}")

def count_string():
    for n in "abcd":
        print(f"string is: {n}")

thread_num=threading.Thread(target=count_num)
thread_string=threading.Thread(target=count_string)

thread_num.start()
thread_string.start()

thread_num.join()
thread_string.join()

print('threading completed')
