import random


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)  # this create the initial condition
        d[c] += 1
    return d


def print_hist(h):
    for i in sorted(histogram(h)):
        print(i, histogram(h)[i])


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('no value avails')


known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


def dict_store():
    fin = open('D:\word.txt')
    d = dict()
    for i in fin:
        d[i.strip()] = None
    return d


def in_dict(string):
    return string in dict_store()


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def in_acker_set(n):
    s = dict()
    for i in range(n):
        s[i + 1] = [0, i]
    return s


cache = {}


def acker(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return acker(m - 1, 1)
    elif (m, n) in cache:  # the book hasn't tell about ordered pair actually
        return cache[m, n]
    else:
        cache[m, n] = acker(m - 1, acker(m, n - 1))
        return cache[m, n]


def has_duplicate(t):  # the solution used set() funtion, again, hasn't appeared
    t = histogram(t)
    for i in t:
        if t[i] > 1:
            return True
    return False


from rotate_word import rotate_word

d=dict_store()
def rotate_list():
    s=dict()
    for key in d:
        for n in range(1,26):
            rot=rotate_word(key,n)
            if rot in d:
                s.setdefault(n,[]).append((key,rot))
    return s

print(rotate_list())
