class PriorityQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def enqueue(self, item, priority):
        if len(self.queue) >= self.size:
            print("Queue is full!")
            return
        self.queue.append((priority, item))
        self.queue.sort()

    def dequeue(self):
        if not self.queue:
            print("Queue is empty!")
            return
        pr, item = self.queue.pop(0)   # remove highest priority
        print(f"Dequeued: {item} (priority {pr})")
        self.display()

    def display(self):
        if not self.queue:
            print("Queue is empty!")
        else:
            print("\nCurrent Queue:")
            for p, item in self.queue:
                print(f"{item} (priority {p})")

size = int(input("Enter queue size: "))
pq = PriorityQueue(size)

print("\nPriority Queue Menu:")
print("Type 'enqueue' to add a task.")
print("Type 'dequeue' to remove the highest priority task.")
print("Type 'display' to show current queue.")
print("Type 'exit' to quit.\n")

while True:
    cmd = input("Enter command: ").strip().lower()
    if cmd == "exit":
        print("Exiting...")
        break
    elif cmd == "enqueue":
        if len(pq.queue) >= pq.size:
            print("Queue is full! Dequeue something first.")
        else:
            item = input("Enter task name: ").strip()
            try:
                priority = int(input("Enter priority (lower number = higher priority): ").strip())
                pq.enqueue(item, priority)
            except ValueError:
                print("Invalid priority. Please enter an integer.")
    elif cmd == "dequeue":
        pq.dequeue()
    elif cmd == "display":
        pq.display()
    else:
        print("Invalid command. Please type 'enqueue', 'dequeue', 'display', or 'exit'.")




"""
# ---- main ----
size = int(input("Enter queue size: "))
pq = PriorityQueue(size)

print("\nEnter tasks one by one.")
print("Type 'done' when finished or when queue is full.\n")

while len(pq.queue) < pq.size:
    item = input("Enter task name (or 'done'): ").strip()
    if item.lower() == "done":
        break
    try:
        priority = int(input("Enter priority: ").strip())
    except ValueError:
        print("Invalid priority. Please enter an integer.")
        continue

    pq.enqueue(item, priority)

pq.display()

# Continuous menu
while True:
    cmd = input("\nEnter 'deque' to remove, 'append' to add, or 'exit' to quit: ").strip().lower()

    if cmd == "exit":
        print("Exiting...")
        break
    elif cmd == "deque":
        pq.dequeue()
    elif cmd == "append":
        if len(pq.queue) >= pq.size:
            print("Queue is full! Dequeue something first.")
        else:
            item = input("Enter task name: ").strip()
            try:
                priority = int(input("Enter priority: ").strip())
                pq.enqueue(item, priority)
            except ValueError:
                print("Invalid priority. Please enter an integer.")
            pq.display()
    else:
        print("Invalid command. Please type 'deque', 'append', or 'exit'.")


# ---- main ----
size = int(input("Enter queue size: "))
pq = PriorityQueue(size)

data = input(
    "Enter pairs: item1 priority1 item2 priority2 ...\n"
    "Example: A 3 B 1 C 2\n> "
).split()

if len(data) % 2 != 0:
    print("Error: please enter pairs. e.g. A 3 B 1 C 2")
else:
    for i in range(0, len(data), 2):
        try:
            pq.enqueue(data[i], int(data[i+1]))
        except ValueError:
            print(f"Invalid priority for '{data[i]}': '{data[i+1]}' is not an integer.")

    pq.display()

    ans = input("\nDequeue one item? (y/n): ").lower()
    if ans in ("y", "yes"):
        pq.dequeue()
    else:
        print("Exit...")
"""