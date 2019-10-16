# 假如这里有 n 个台阶，每次你可以跨 1 个台阶或者 2 个台阶，请问走这 n 个台阶有多少种走法？
import functools
import time


def calcu_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        print('cost time {}'.format(time.time()-start_time))
    return wrapper


# 最原始版本
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n-1) + f(n-2)


# 解决重复计算问题
def f2(n):
    fn_dict = {}
    if n == 1:
        return 1
    if n == 2:
        return 2
    if fn_dict.get(n):
        return fn_dict[n]
    res = f2(n-1) + f2(n-2)
    fn_dict[n] = res
    return res


# 非递归实现  这块得想明白
def f_not_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    ret, pre, prepre = 0, 2, 1
    for i in range(3, n+1):
        ret = pre + prepre
        prepre = pre
        pre = ret
    return ret


if __name__ == '__main__':
    start_time = time.time()
    res = f_not_recursive(6)
    print('cost time {}'.format(time.time()-start_time))
    print(res)
