import time
import threading
class StoppableThread(threading.Thread):
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
            i%=4
            if not T.is_alive():
                self.stop()
            out = ""
            if i == 0:
                out = "-"
            elif i == 1:
                out = "\\"
            elif i == 2:
                out = "|"
            elif i == 3:
                out = "/"
            print(f"%s"%(out), end="", flush=True)
            time.sleep(0.1)
            print ("\n\033[A                             \033[A", flush = True)
