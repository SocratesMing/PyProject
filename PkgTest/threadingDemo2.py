import threading,time,logging
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-10s) %(message)s')
# event test

def wait_for_event(e):

    logging.debug("wait for event start")
    event_is_set = e.wait()
    logging.debug("event set: %s", event_is_set)


def wait_for_event_timeout(e,t):
    while not e.isSet():
        logging.debug("wait for event timeout start")
        event_is_set = e.wait(t)
        logging.debug("event set: %s",event_is_set)
        if event_is_set:
            logging.debug("processing event")
        else:
            logging.debug("doing other work")

e = threading.Event()
t1 = threading.Thread(name='block',target=wait_for_event,args=(e,))

t1.start()
t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e,2))
t2.start()
logging.debug('waiting before calling event.set()')
time.sleep(3)
e.set()
logging.debug("Event is set")
