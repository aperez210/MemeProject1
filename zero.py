import sys
import logging
import one,three

arguments = sys.argv
n = len(arguments)

if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    if arguments[1] == "s":
        logging.disable()
    logging.info("Starting.")
    y = three.LoadingThread()
    x = three.threading.Thread(target=one.Start, args=())
    x.start()
    y.Start(T=x)
    logging.info("Waiting for query.")

    x.join()
    logging.info("Done!")
