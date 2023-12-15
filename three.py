import time
import threading
class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.group = None
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

class LoadingThread(StoppableThread):
    def Start(self,T):
        i = 0
        time.sleep(.25)
        while not self.stopped():
            
            i+=1
            n = i%4
            if not T.is_alive():
                self.stop()
            out = ""
            
            if n == 0:
                out = "-"
            elif n == 1:
                out = "\\"
            elif n == 2:
                out = "|"
            elif n == 3:
                out = "/"
            print(f"%s"%(out), end="", flush=True)
            time.sleep(0.25)
            print ("\n\033[A                             \033[A", flush = True)
