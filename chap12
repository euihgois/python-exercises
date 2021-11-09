from chap_11 import histogram, dict_store
from chap10 import is_anagram


def sumall(*args):
    return sum(args)


s = [1, 2, 5, 3]
b = [2, 2, 1, 5]


def has_match(a, b):
    for x, y in zip(a, b):
        if x == y:
            return True
    return False


def most_frequent(str):
    d = histogram(str).items()
    t = list()
    for i, n in d:
        t.append((n, i))
    for n, i in reversed(sorted(t)):
        print(n, i)


def list_anagram(c): #many modification from solution, it's shorter
    d = dict_store()
    nd = dict()  # new dict
    k=list()
    s=''
    for i in d:
        t=s.join(sorted(i))
        nd.setdefault(t,[]).append(i) #setdefault method actually referring to the actual value
    for i in nd.values(): #which faster: values method or just mapping the values?
        l=len(i)
        if l>c:
            k.append((l,i))
    for i in reversed(sorted(k)):
        print(list(i))
    return None

def all_anagram():  #this only for all_methasis
    d = dict_store()
    nd = dict()
    s = ''
    k=list()
    m=dict()
    for i in d:
        t = s.join(sorted(i))
        nd.setdefault(t, []).append(i)
    for j in nd.values():
        if len(j)>1:
            k.append(j)
    return k

def count_diff(str1,str2):
    c=0
    if sorted(str1)!=sorted(str2):
        return -1
    for x,y in zip(str1,str2):
        if x!=y:
            c+=1
    return c

def is_methasis(str1,str2):
    return count_diff(str1,str2)==2


def all_methasis():
    a=all_anagram()
    c=0
    for i in a:
        length=len(i)
        for j in range(length):
            for k in range(j+1,length):
                u, o =i[j], i[k]
                if is_methasis(u,o):
                    c+=1
                    print(u,o)
    print(c)

def children(s):
    k=list(s)
    d=''
    nk=list()
    for i in range(len(s)):
        temp=k[:]
        temp.pop(i)
        h=d.join(temp)
        if h in dicti:
            nk.append(h)
    return nk


known=dict()
def dict_all_child():
    for i in dicti:
        k=children(i)
        if k!=[]:
            known[i]=k
    return known

def is_reducible(s):
    if s in known:
        if known[s]==['']:
            return True
        k=list()
        for i in known[s]:
            val=is_reducible(i)
            k.append(val)
        return True in k
    return False

def create_all_children():
    k=list()
    for i in known:
        if is_reducible(i):
            k.append(tuple([len(i),i]))
    return sorted(k)


def list_child(t): #unneeded
    if t=={} or '' in t or len(t)==1:
        return list(t)
    for i in t:
        pass
    return list(list_child(t))

nd = dict()
def create_all_child(): #tester, unneeded
    global nd
    for i in dicti:
        y=list_child(children(i))
        if is_reducible(y):
            nd[i]=y
        print(nd)
    return nd

def is_reducible1(l): #tester, unneeded
    if s in known:
        for i in known[s]:
            return is_reducible(i)
    if '' in l and len(l)>1:
        return True
    return False

def create_all_reducible(d): #tester, unneeded
    l=list()
    for i in d:
        if is_reducible(d[i]):
            l.append(tuple(len(i),i))
    return sorted(l)

dicti = dict_store()
dict_all_child()
