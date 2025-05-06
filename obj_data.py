# list  
list = [1,2,[3,4,'hello']]
list[2][2] = 'goodbye'
print(list) 

list = [5,3,7,1]
print(sorted(list))

#dictionary 
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#tuples 
tupl = (1,2,3) 

#sets
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))