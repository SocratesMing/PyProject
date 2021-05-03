import threading,time,logging
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')
def daemon():
    logging.debug("start daemon")
    time.sleep(2)
    logging.debug("stop daemon")

def Notdaemon():
    logging.debug("start not daemon")
    logging.debug("stop not daemon")

d = threading.Thread(name="daemon",target=daemon)
d.setDaemon(True)

nt = threading.Thread(name="Not daemon",target=Notdaemon)
d.start()
nt.start()
d.join()
