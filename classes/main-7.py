#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self._q = list()

# Press the green button in the gutter to run the script.
    def insert(self, value):
        self._q.append(value)
        return value
    def remove(self):
        try:
            self._q[0]
        except:
            print('The queue is empty')
        else:
            print(self._q.pop(0))


def main():
    queue = Queue()
    queue.insert(5)
    queue.insert(6)
    queue.remove()
    queue.insert(7)
    queue.remove()
    queue.remove()
    queue.remove()


if __name__ == '__main__': main()