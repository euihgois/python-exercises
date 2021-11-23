import time

def nested_sum(t):
    c=0
    for i in t:
        c+=sum(i)
    return print(c)

def cumsum(t):
    s=[]
    for i in range(len(t)):
        s.append(sum(t[:i+1])) #this doesn't return a value
    return print(s)

def chop(t):
    del t[0],t[len(t)-1]

def middle(t):
    return t[1:len(t)]

def is_sorted(t):
    for i in range(len(t)):
        if t[i]!=sorted(t)[i]:
            return False
    return True

def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False
    for i in range(len(str1)):
        if sorted(str1)[i]!=sorted(str2)[i]:
            return False
    return True

def has_duplicate(t):
    for i in range(len(t)):
        if t[i] in t[i+1:]:
            return True
    return False

def same_birthday(n,c):
    import random
    a=0
    b=0
    for i in range(n):
        t=[]
        for j in range(c):
            t.append(random.randint(1,365))
        if has_duplicate(t):
            a+=1
        else:
            b+=1
    return print("here's the chance:",a/n*100,'%')

def append_read():
    fin = open('D:\word.txt')
    s=[]
    for i in fin:
        word=i.strip()
        s.append(word)
    return s

def idiom_read():
    fin = open('D:\word.txt')
    s = []
    for i in fin:
        word = i.strip()
        s+=[word]
    return s

def search_index(t,val):
    pass

def in_ord(t,val):
    return val in t

def in_bisect(t,val):
    if len(t)==0:
        return False
    if t[len(t)//2]==val:
        return True
    elif t[len(t)//2]>val:
        return in_bisect(t[:len(t)//2],val)
    elif t[len(t)//2]<val:
        return in_bisect(t[len(t)//2+1:],val)


def execution_time(f,t):
    t=sorted(t)
    t0=time.time()
    f(t)
    t1=time.time()
    return print('heres the time:',float(t1-t0),'for',f)

def is_reverse(s1,s2):
    return s1==s2[::-1]

def rpairs_list(t):
    for i in range(len(t)):
        if in_bisect(t[i+1:],t[i][::-1]):
            print(t[i],t[i][::-1])

def rpairs_list1(t):
    for i in t:
        if in_bisect(t,i[::-1]):
            print(i,i[::-1])
def reverse_word(s):
    return s[::-1]

def interlock_list(t):
    for i in t:
        if len(i)%2==0:
            str1=i[::2]
            str2=reverse_word(i[::-2])
            if in_bisect(str1) and in_bisect():
                pass #accidentally deleted


