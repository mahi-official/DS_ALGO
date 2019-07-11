from collections import namedtuple

a = namedtuple('courses', 'name, tech, place')
s = a('mahesh', 'python', 'delhi')
t = a._make(['neha', 'go', 'delhi'])

print(s)
print(t)

#####################################################################
from collections import deque

a = ['e', 'd', 'u', 't', 'a', 'm', 'h']
d = deque(a)

d.appendleft('w') #append at begining
d.append('w') #append at last
print(d)

d.pop() #pop from last
d.popleft() #pop from start

print(d)

#####################################################################
from collections import ChainMap

a = {1:'Mahesh', 2:'Python'}
a = {1:'Neha', 2:'GoLang'}

c = ChainMap(a,b)
print(c)

#####################################################################
from collections import Counter

a = [1,2,3,4,5,6,12,3,2,1,3,5,6,2,1,1,13,2]
cnt = Counter(a) #counts no. of elements
print(cnt)
print(list(cnt.elements())) #print sorted list
print(c.most_common())

#####################################################################
from collections import OrderedDict

o =  OrderedDict()
o[1] = 'm'
o[2] = 'a'
o[3] = 'h'
o[4] = 'e'
o[5] = 's'
o[6] = 'h'

d[1] = 'k'
d[3] = 'l'

print(o)

#####################################################################
from collections import defaultdict

dd = defaultdict()

dd[1] = 'python'
dd[2] = 'edureka'
dd[3] = 'java'
dd[4] = 'andrew'

print(dd)
print(dd[7])
