# NOTE: 进程和线程的区别
#  在CPython中，由于存在GIL（全局解释器锁），同一时刻只有一个线程能执行
#  I/O密集型应用可使用多线程模型
#  计算密集型应用应当使用多进程模型
from multiprocessing import Queue, Pipe

# NOTE: 多进程通信

# NOTE: 队列
q = Queue(3)
q.put(1)
q.put(2)
q.put(3)
# q.put(4)
q.get()
print(q.full())
print(q.empty())
print(q.qsize())

# NOTE: 管道
a, b = Pipe()

a.send([1, 'hello', None])
print(b.recv())

b.send(b'thank you')
print(a.recv())

# NOTE: 共享内存
