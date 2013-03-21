# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which
#    should be 10
#
# Your test function should run assertion checks and throw an
# AssertionError for each of the 5 incorrect Queues. Pressing
# submit will tell you how many you successfully catch so far.

import array

class Queue:
  def __init__(self, size_max):
    assert size_max > 0
    self.max = size_max
    self.head = 0
    self.tail = 0
    self.size = 0
    self.data = array.array('i', range(size_max))

  def empty(self):
    return self.size == 0

  def full(self):
    return self.size == self.max

  def enqueue(self, x):
    if self.size == self.max:
      return False
    self.data[self.tail] = x
    self.size += 1
    self.tail += 1
    if (self.tail == self.max):
      self.tail = 0
    return True

  def dequeue(self):
    if (self.size == 0):
      return None
    x = self.data[self.head]
    self.head += 1
    self.size -= 1
    if (self.head == self.max):
      self.head = 0
    return x

  def checkrep(self):
    assert self.size >= 0 and self.size <= self.max
    if self.tail > self.head:
      assert (self.tail - self.head) == self.size
    if self.tail < self.head:
      assert (sefl.max - self.head + self.tail) == self.size
    if (self.head == self.tail):
      assert self.size == 0 or self.size == self.max

def test1():
  q = Queue(3)
  if not q.empty():
    print "test1 FAILED"
    return

  if not q.enqueue(10):
    print "test1 FAILED"
    return

  if not q.enqueue(11):
    print "test1 FAILED"
    return

  if 10 != q.dequeue():
    print "test1 FAILED"
    return

  if 11 != q.dequeue():
    print "test1 FAILED"
    return

  if not q.empty():
    print "test1 FAILED"
    return

  q.checkrep()
  print "test1 PASSED"

def test2():
  q = Queue(1)
  q.enqueue(1)
  if q.enqueue(2):
    print "test2 FAILED"
    return

  q.checkrep()
  print "test2 PASSED"

def test3():
  q = Queue(1)
  if None != q.dequeue():
    print "test3 FAILED"
    return

  q.checkrep()
  print "test3 PASSED"

def test4():
  for t in range(100):
    random.seed(t)
    maxsize = random.randint(1, 1000)
    q = Queue(maxsize)
    qsize = 0
    for i in range(10000):
      r = random.randint(1, 1000)
      method = r % 4
      q.checkrep()
      if method == 0:
        assert q.empty() == (qsize == 0)
      elif method == 1:
        assert q.full() == (qsize == maxsize)
      elif method == 2:
        if q.enqueue(r):
          qsize += 1
      elif method == 3:
        if q.dequeue() != None:
          qsize -= 1

  print "test4 PASSED"

def test5():
  q = Queue(1)
  if not q.empty():
    print "test5 FAILED"
    return
  if not q.enqueue(10):
    print "test5 FAILED"
    return
  if not q.full():
    print "test5 FAILED"
    return
  if 10 != q.dequeue():
    print "test5 FAILED"
    return

  q.checkrep()
  print "test5 PASSED"

def main():
    test1()
    test2()
    test3()
    test4()
    test5()

if __name__ == '__main__':
    main()
