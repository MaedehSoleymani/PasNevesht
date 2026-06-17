import threading

def run_async(func, *args, **kwargs):
    threading.Thread(target=func, args=args, kwargs=kwargs).start()