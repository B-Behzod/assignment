print(4 * (6 + 5))
print(4 * 6 + 5 )
print(4 + 6 * 5 )

a = 3 + 1.5 + 4
print(type(a))

b = 'hello'
print(b[1])
print(b[::-1])
print(b[4])
print(b[-1])

list = [0, 0, 0]
print(list)

d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
d = {'k1':[{'nest key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest key'][1][0])
#d = {'k1':[1,2,{'k2'['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print(d['k1'])

t = (5,8,9)
print(t)

list5 =[1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

e = 2 > 3
print(e)
e = 3 <= 2
print(e)
e = 3 == 2.0
print(e) 
e = 3.0 == 3
print(e)
e = 4**0.5 != 2
print(e)
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
print(l_one[2][0] >= l_two[2]['k1'])
