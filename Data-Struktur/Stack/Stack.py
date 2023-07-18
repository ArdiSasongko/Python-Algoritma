class Stack:
    def __init__(self):
        self.stack = []
    
    def empty(self):
        return True if len(self.stack) == 0 else False
    
    def push(self, item):
        self.stack.append(item)

    def get_stack(self):
        return self.stack
    
    def pop(self):
        return None if self.empty() else self.stack.pop()

stack = Stack()

i = int(input("Masukkan banyak stack yang ingin diinput: "))
for y in range(i):
    print("Stack ke:", y)
    j = int(input("Masukkan nilai: "))
    stack.push(j)

print(stack.get_stack())
print("Pop : ",stack.pop())
print(stack.get_stack())
