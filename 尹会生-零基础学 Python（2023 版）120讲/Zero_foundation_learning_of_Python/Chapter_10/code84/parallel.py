# NOTE: 利用concurrent实现并行计算
#  concurrent.futures库中的Executor对象是并行任务的抽象类
#  它可以由线程和进程两种方式实现并行计算
#  Executor可以通过submit()方式执行
#  Executor对象还支持ThreadPoolExecutor方式，使用线程池实现并发
#  还支持ProcessPoolExecutor方式，以使用多核CPU
import concurrent.futures
import urllib.request

URLS = ['http://www.baidu.com/',
        'http://www.baidu.com/',
        'http://www.baidu.com/',
        'http://www.baidu.com/',
        'http://www.baidu.com/']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future_to_url = {executor.submit(load_url(url, 60)): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = bytes(future.result(), 'utf-8')
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
