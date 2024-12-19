import threading


def one():
    """Prints "One" to the console."""
    for i in range(50):
        print("One")

def two():
    """Prints "Two" to the console."""
    for i in range(50):
        print("Two")


t1 = threading.Thread(target=one)
t2 = threading.Thread(target=two)

t1.start()
t2.start()
