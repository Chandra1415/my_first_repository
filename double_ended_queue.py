class Deque:
    def __init__(self, size):
        self.deque = []
        self.size = size

    def insert_front(self, item):
        if len(self.deque) >= self.size:
            print("Deque is full!")
            return
        self.deque.insert(0, item)
        self.display()

    def insert_rear(self, item):
        if len(self.deque) >= self.size:
            print("Deque is full!")
            return
        self.deque.append(item)
        self.display()

    def delete_front(self):
        if not self.deque:
            print("Deque is empty!")
            return
        print(f"Removed from front: {self.deque.pop(0)}")
        self.display()

    def delete_rear(self):
        if not self.deque:
            print("Deque is empty!")
            return
        print(f"Removed from rear: {self.deque.pop()}")
        self.display()

    def display(self):
        if not self.deque:
            print("Deque is empty!")
        else:
            print("Deque contents:", *self.deque)


# ---- main ----
size = int(input("Enter deque size: "))
dq = Deque(size)

while True:
    cmd = input("\nChoose: insert_front, insert_rear, delete_front, delete_rear, display, exit\n> ").strip().lower()

    if cmd == "exit":
        print("Exiting...")
        break
    elif cmd == "insert_front":
        dq.insert_front(input("Enter value: "))
    elif cmd == "insert_rear":
        dq.insert_rear(input("Enter value: "))
    elif cmd == "delete_front":
        dq.delete_front()
    elif cmd == "delete_rear":
        dq.delete_rear()
    elif cmd == "display":
        dq.display()
    else:
        print("Invalid command!")
