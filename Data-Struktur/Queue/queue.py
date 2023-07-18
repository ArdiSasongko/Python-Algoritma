class Queue():
    def __init__(self):
        self.queue = []
    
    def empty(self):
        return True if len(self.queue) == 0 else False
    
    def get_queue(self):
        return self.queue
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return None if self.empty() else self.queue.pop(0)
    
queue = Queue()

i = int(input("Masukkan banyak antria yang ingin diinput: "))
for y in range(i):
    print("antrian ke:", y)
    j = int(input("Masukkan nilai: "))
    queue.enqueue(j)

print(queue.get_queue())
print("Pop : ",queue.dequeue())
print(queue.get_queue())

    