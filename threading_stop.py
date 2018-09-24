import threading
import time
'''
shows how to properly stops a while True looping thread safely
uses thread event to stop the loop
'''
def main():

    t1_stop = threading.Event()
    t1 = threading.Thread(target=thread1, args=(1,t1_stop))
    t1.start()

    time.sleep(10)
    t1_stop.set()

def thread1(arg1,stop_event):
    x=0
    print('thread1 started')
    while not stop_event.is_set():
        print ('thread1 running' + str(x))
        x += 1
        stop_event.wait(timeout=1)
        

if __name__ == '__main__':
    main()
