# -*- coding: utf-8 -*-
"""
A timeout decorator.

Usage:
@timeout(4)
def timeout_test():
    time.sleep(10)

From: http://zhuanlan.zhihu.com/auxten/20175869

著作权归作者所有。
商业转载请联系作者获得授权，非商业转载请注明出处。
作者：auxten
链接：http://zhuanlan.zhihu.com/auxten/20175869
来源：知乎
"""

import signal
import functools
class TimeoutError(Exception): pass #定义一个Exception，后面超时抛出 

def timeout(seconds, error_message = 'Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated
