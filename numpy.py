import numpy as np

a=np.arange(10,50)
print(f"a : \n{a}")

b=a[::-1]
print(f"b : \n{b}")

c=np.random.random((3,3))
print(f"c :\n{c}")

d=[1,3,0,0,9,0,4]
d=np.nonzero(d)
print(f"d :\n{d}")

e=np.eye(3)
print(f"e :\n{e}")

f=np.random.random((3,3,3))
print(f"f :\n{f}")

g=np.random.random((10,10))
gmin,gmax=g.min(),g.max()
print(f"g :\n{g}")
print(f"gmin : {gmin}, gmax : {gmax}")

h=np.random.random((30))
print(f"h :\n{h}")
hmean=h.mean()
print(f"hmean : {hmean}")

i=np.ones((4,4))
i[1:-1,1:-1]=0
print(f"i :\n{i}")

j=np.pad(i,pad_width=1,mode="constant",constant_values=0)
print(f"j :\n{j}")

k=np.dot(np.ones((5,3)),np.ones((3,2)))
print(f"k :\n{k}")

l=np.arange(11)
l[4:9]*=-1
print(f"l :\n{l}")

m1=np.random.randint(0,10,10)
m2=np.random.randint(0,10,10)
print(f"m1 :\n{m1}")
print(f"m2 :\n{m2}")
m=np.intersect1d(m1,m2)
print(f"m :\n{m}")

n_yesterday=np.datetime64('today','D')-np.timedelta64(1,'D')
n_today=np.datetime64('today','D')
n_tomorrow=np.datetime64('today','D')+np.timedelta64(1,'D')
print(f"n_yesterday : {n_yesterday}")
print(f"n_today : {n_today}")
print(f"n_tomorrow : {n_tomorrow}")

o=np.arange('2016-07','2016-08',dtype='datetime64[D]')
print(f"o :\n{o}")

p1=np.array([1.0, 2.0, 3.0])
p2=np.array([1.0, 2.000001, 3.0])
p3=np.allclose(p1,p2) #checks with tolerance by relative(rtol) and absolute(atol) value
p4=np.array_equal(p1,p2) #strictly checks without tolerance
print(f"p1 :\n{p1}")
print(f"p2 :\n{p2}")
print(f"p3 : {p3}")
print(f"p4 : {p4}")

q=np.random.randint(0,10,10)
print(f"q :\n{q}")
q[q.argmax()]=0
print(f"q :\n{q}")
