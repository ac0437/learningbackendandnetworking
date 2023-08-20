import threading

def hello_world():
    print("hello world")
    return "hello world"

for i in range(10):
    thread = threading.Thread(target=hello_world)
    thread.start()