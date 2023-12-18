import sys
import logging
import one,three

arguments = sys.argv
n = len(arguments)

if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    try:
        if arguments[1] == "s":
            logging.info("logging disabled")
            logging.disable()
    except:
        logging.info("Logging enabled.")
    logging.info("Starting.")
    y = three.LoadingThread()
    x = three.threading.Thread(target=one.Start, args=())
    logging.info("Waiting for query.")
    x.start()
    y.Start(T=x)

    x.join()
    logging.info("Done!")
