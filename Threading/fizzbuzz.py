from queue import Queue

queue = Queue()
for i in range(100):
    queue.put(i)

    if not queue.empty():
        num = queue.get()

        if (num % 3) == 0 and (num % 5) == 0:
          print("Fizzbuzz")
        elif (num % 3) == 0:
          print("Fizz")
        elif (num % 5) == 0:
          print("Buzz")

